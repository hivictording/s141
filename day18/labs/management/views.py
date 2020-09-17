from django.shortcuts import render,HttpResponse,redirect
from management import models
from management.models import ApplicationsnForm

# Create your views here.

import json

def login(request):
    err_msg = ''
    if request.method == 'POST':
        u = request.POST.get('username',None).strip()
        p = request.POST.get('password',None).strip()

        if not u or not p:
            err_msg = "username or password can't be empty"
        else:
            user = models.Users.objects.filter(username=u).first()
            if user:
                if user.password == p:
                    page = redirect('/labs/home/')
                    # page.set_cookie("username",u)
                    page.set_signed_cookie("username",u,salt='aaa')
                    return page
                else:
                    err_msg = 'Wrong password for user "{}"'.format(u)
            else:
                err_msg = "User '{}' does not exist in the database".format(u)
    return render(request, 'management/login.html', {'error_message':err_msg})

def home(request):
    v = request.COOKIES.get("username")
    # v = request.get_signed_cookie("username",salt='aaa')
    if not v:
        return redirect('/labs/login/')
    else:
        if request.method == 'POST':
            # Handle File Upload
            file = request.FILES.get('file',None)
            with open(file.name,"wb") as f:
                for i in file.chunks():
                    f.write(i)

        values = models.Hosts.objects.all().values('id','name','ip','netmask','type','location','reg_date','owner_id','owner__username')

    # for value in values:
    #     print(value.id,value.name)

    return render(request, 'management/home.html', {'hosts': values, 'users': models.Users.objects.all(), })
    # return render(request,'home.html',{'hosts':models.Hosts.objects.all(),'users':models.Users.objects.all(),})


def ajax(request):
    ret = {"status":True,"err_msg":None,"data":None}

    if request.method == 'POST':
        name = request.POST.get('host_name', None).strip()
        ip = request.POST.get('host_ip', None).strip()
        netmask = request.POST.get('host_netmask', None).strip()
        type = request.POST.get('host_type', None).strip()
        owner = request.POST.get('host_owner', None).strip()
        location = request.POST.get('host_location', None).strip()

        owner_id = models.Users.objects.filter(id=owner).first()
        if owner_id:
            models.Hosts.objects.create(name=name,ip=ip,netmask=netmask,type=type,owner_id=owner,location=location)
        else:
            ret["status"] = False
            ret['err_msg'] = 'Owner does not exist'


    return HttpResponse(json.dumps(ret))

def ajax_edit(request):
    ret = {"status":True,"err_msg":None,"data":None}

    if request.method == 'POST':
        id = request.POST.get('host_id',None)
        name = request.POST.get('host_name', None).strip()
        ip = request.POST.get('host_ip', None).strip()
        netmask = request.POST.get('host_netmask', None).strip()
        type = request.POST.get('host_type', None).strip()
        owner = request.POST.get('host_owner', None).strip()
        location = request.POST.get('host_location', None).strip()
        # reg_date = request.POST.get('host_reg_date', None).strip()

        models.Hosts.objects.filter(id=id).update(name=name,ip=ip,netmask=netmask,type=type,owner=owner,location=location)


    return HttpResponse(json.dumps(ret))

def ajax_del(request):
    ret = {"status":True,"err_msg":None,"data":None}

    if request.method == 'POST':
        id = request.POST.get('host_id',None)
        print(id)

        models.Hosts.objects.filter(id=id).delete()


    return HttpResponse(json.dumps(ret))

def user(request,uid):
    obj = models.Users.objects.filter(id=uid).first()

    user = {}

    if obj:
        user['id'],user['username'],user['age'],user['gender'],user['role'] = \
            obj.id,obj.username,obj.age,obj.gender,obj.role

    return  render(request, 'management/user.html', {'user':user})

def user_get(request):
    if request.method == 'GET':
        uid = request.GET.get('uid',None)

    obj = models.Users.objects.filter(id=uid).first()

    # user = {}
    #
    # if obj:
    #     user['id'], user['username'], user['age'], user['gender'], user['role'] = \
    #         obj.id, obj.username, obj.age, obj.gender, obj.role

    return render(request, 'management/user.html', {'user': obj})

def apps(request):
    if request.method == 'GET':
        # obj_app = models.Applications.objects.all().values('name','owner_id','platform','host','owner__username')
        obj_app = models.Applications.objects.all()
        owner_names = models.Applications.objects.all().values('owner__username')
        alist,hlist,olist = [],[],[]
        # form = ApplicationsForm()

        for o in owner_names:
            olist.append({'owner_name':o['owner__username']})

        for a in obj_app:
            hlist = []
            for h in a.host.all():
                hlist.append(h.name)
            alist.append({'name': a.name, 'owner_id': a.owner_id, 'platform': a.get_platform_display, 'host': hlist})

        for i in range(len(alist)):
            alist[i].update(olist[i])

    all_users = models.Users.objects.all()

    app_form = ApplicationsnForm()

    all_hosts = models.Hosts.objects.all()

    for h in all_hosts:
        print(h)

    # for k,v in request.environ.items():
    #     print(k,v)

    return render(request, 'management/apps.html', {'apps':alist, 'users':all_users, 'app_form':app_form, 'hosts':all_hosts, 'obj':obj_app, "envs":request.environ})

def apps1(request):
    if request.method == 'GET':
        obj_app = models.Applications.objects.all()
        all_users = models.Users.objects.all()
        app_form = ApplicationsnForm()
        all_hosts = models.Hosts.objects.all()

    return render(request, 'management/apps1.html', {'users':all_users, 'app_form':app_form, 'hosts':all_hosts, 'obj':obj_app, "envs":request.environ})

def appAdd(request):
    ret = {'status':True,'err_msg':None,'data':None}

    if request.method == 'POST':
        appname = request.POST.get('appname',None)
        username = request.POST.get('username',None)
        platform = request.POST.get('platform', None)
        hosts = request.POST.getlist('hostname', None)

        app_list = [app.name.lower() for app in models.Applications.objects.all()]

        if appname.lower() not in app_list:
            newrow = models.Applications.objects.create(name=appname, owner_id=username, platform=platform)
            # create也可以用如下两句代替
            # newrow = models.Applications(name=appname, owner_id=username, platform=platform)
            # newrow.save()
            newrow.host.add(*hosts)
        else:
            ret['status'] = False
            ret['err_msg'] = 'App {} already in the backend database!'.format(appname)

    return HttpResponse(json.dumps(ret))