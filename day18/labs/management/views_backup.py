from django.shortcuts import render,HttpResponse,redirect
from django.views import View

# Create your views here.

from sqlalchemy import create_engine,ForeignKey,Index,Column,ForeignKeyConstraint,DateTime,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
import json

db = create_engine('mysql+pymysql://vding:password@192.168.2.22/labs',echo=True)
db.connect()
session = sessionmaker(bind=db)
session = session()
base = declarative_base()

class Users(base):
    __tablename__ = 'users'
    id = Column('id',mysql.INTEGER,primary_key=True,autoincrement=True)
    username = Column('username',mysql.VARCHAR(12),nullable=False)
    password = Column('password',mysql.VARCHAR(12),nullable=False)

class Hosts(base):
    __tablename__ = 'hosts'
    __table_args__ = (ForeignKeyConstraint(['owner_id'], ['users.id']),)
    id = Column('id',mysql.INTEGER,primary_key=True,autoincrement=True)
    name = Column('name',mysql.VARCHAR(15),nullable=False)
    ip = Column('ip',mysql.VARCHAR(15),nullable=False)
    netmask = Column('netmask',mysql.VARCHAR(15),nullable=False)
    type = Column('type',mysql.VARCHAR(20),nullable=False,default='Cisco IOS')
    owner_id = Column('owner_id',mysql.INTEGER,nullable=False)
    location = Column('location',mysql.VARCHAR(15),nullable=False,default="Toronto")
    reg_date = Column('reg_date',mysql.TIMESTAMP,default=func.now(),nullable=False)

base.metadata.create_all(db)

# class Login(View):
#     def post(self,request):
#         err_msg = ''
#         if request.method == 'POST':
#             u = request.POST.get('username', None).strip()
#             p = request.POST.get('password', None).strip()
#
#             if not u or not p:
#                 err_msg = "username or password can't be empty"
#             else:
#                 user = session.query(Users).filter_by(username=u).first()
#                 if user:
#                     if user.password == p:
#                         return redirect('/home/')
#                     else:
#                         err_msg = 'Wrong password for user "{}"'.format(u)
#                 else:
#                     err_msg = "Can't find user '{}' in the database".format(u)
#         return render(request, 'login.html', {'error_message': err_msg})

def login(request):
    err_msg = ''
    if request.method == 'POST':
        u = request.POST.get('username',None).strip()
        p = request.POST.get('password',None).strip()

        if not u or not p:
            err_msg = "username or password can't be empty"
        else:
            user = session.query(Users).filter_by(username=u).first()
            if user:
                if user.password == p:
                    return redirect('/labs/home/')
                else:
                    err_msg = 'Wrong password for user "{}"'.format(u)
            else:
                err_msg = "Can't find user '{}' in the database".format(u)
    return render(request, 'management/login.html', {'error_message':err_msg})

def home(request):
    if request.method == 'POST':
        # Handle File Upload
        file = request.FILES.get('file',None)
        with open(file.name,"wb") as f:
            for i in file.chunks():
                f.write(i)

    hosts = [{'id': host.id, 'name': host.name, 'ip': host.ip, 'netmask': host.netmask, \
              'type': host.type, 'owner_id': host.owner_id, 'location': host.location, \
              'reg_date': host.reg_date} for host in session.query(Hosts)]

    users = []

    for user in session.query(Users):
        users.append({'user_id':user.id,'user_name':user.username})

    return render(request, 'management/home.html', {'hosts':hosts, 'users':users, })


def ajax(request):
    ret = {"status":True,"err_msg":None,"data":None}

    if request.method == 'POST':
        name = request.POST.get('host_name', None).strip()
        ip = request.POST.get('host_ip', None).strip()
        netmask = request.POST.get('host_netmask', None).strip()
        type = request.POST.get('host_type', None).strip()
        owner = request.POST.get('host_owner', None).strip()
        location = request.POST.get('host_location', None).strip()
        print(name,ip,netmask,type,owner,location)

        owner_id = session.query(Users).filter_by(id=owner).first()
        if owner_id:
            host_single_data = Hosts(name=name, ip=ip, netmask=netmask, type=type, owner_id=owner, location=location)
            session.add(host_single_data)
            session.commit()
        else:
            ret["status"] = False
            ret['err_msg'] = 'Owner does not exist'


    return HttpResponse(json.dumps(ret))





