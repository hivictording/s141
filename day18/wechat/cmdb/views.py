# Create your views here.

from django.shortcuts import HttpResponse,render,redirect

USERS = [{'name':'Victor'+str(i),'age':45-i,'gender':'Male','city':'Tornto'} for i in range(20)]

def index(request):
    return HttpResponse('<h1>Hello Wechat</h1>')

def login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username == 'root' and password == 'root':
            return redirect('/home/')
        else:
            error_msg = "Invalid username or password!"

    return render(request,"login.html",{'error_message':error_msg})

def home(request):
    if request.method == 'POST':
        n = request.POST.get('name',None)
        a = request.POST.get('age', None)
        g = request.POST.get('gender', None)
        c = request.POST.get('city', None)
        USERS.append({'name':n,"age":a,"gender":g,"city":c})
    return render(request,'home.html',{'users':USERS})
