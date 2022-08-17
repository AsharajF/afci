import email
from email import message
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import dashboard,apply_afci
from home.models import gallery
# Create your views here.
def register(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        em=request.POST['email']
        cn=request.POST['contact']
        city=request.POST['city']
        ps=request.POST['pw']
        cps=request.POST['cpw']
        if ps==cps:
            if (User.objects.filter(username=un)).exists():
                messages.info(request,"Username is invalid")
                return redirect('register')
            else:
                accntcrt=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=ps)
                accntcrt.save()
                db=dashboard(us=accntcrt,contactno=cn,city=city)
                db.save()
                return redirect('hm')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
    return render(request,'index-1.html') #earlier register.html was written
# def stregister(request):
#     if request.method=='POST':
#         fn=request.POST['fname']
#         ln=request.POST['lname']
#         un=request.POST['uname']
#         em=request.POST['email']
#         cn=request.POST['contact']
#         city=request.POST['city']
#         ps=request.POST['pw']
#         cps=request.POST['cpw']
#         if ps==cps:
#             if (User.objects.filter(username=un)).exists():
#                 messages.info(request,"Username is invalid")
#                 return redirect('register')
#             else:
#                 accntcrt=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=ps)
#                 if "staff" in request.POST:
#                     accntcrt.is_staff=True
#                     accntcrt.save()
#                 db=dashboard(us=accntcrt,contactno=cn,city=city)
#                 db.save()
#                 return redirect('hm')
#         else:
#             messages.info(request,'Password does not match')
#             return redirect('register')
#     return render(request,'register1.html') 

def Apply_afci(request):
    dis={}
    gall=gallery.objects.all()
    dis["gal"]=gall
    if request.method=='POST':

        fn=request.POST['fname']
        ln=request.POST['lname']
        em=request.POST['email']
        pic=request.POST['profilepic']
        cv=request.POST['cv']
        city=request.POST['city']
        cn=request.POST['contact']
        quali=request.POST['qualification']
        wrkex=request.POST['workex']
        gen=request.POST['gender']
        applyfor=request.POST['Applyfor']
        
        stfaply=apply_afci(f_name=fn,l_name=ln,email=em,profilepic=pic,contactno=cn,city=city,workex=wrkex,quali=quali,gender=gen,cv=cv,applyfor=applyfor) 
        stfaply.save()
        
    return render(request,'apply_afci.html',dis) 

    
def login(request):
    if request.method=='POST':
        un=request.POST['uname']
        pw=request.POST['pw']
        log=auth.authenticate(username=un,password=pw)
        if log!=None:
            auth.login(request,log)
            messages.success(request,"Welcome")
            return redirect('hm')
        else:
            messages.warning(request,"Invalid Username or Password") 
            return redirect('register')   
    return render(request,'index-1.html')

def logout(request):
    auth.logout(request)
    return redirect('hm')

def profile(request):
    dis={}
    gall=gallery.objects.all()
    dis["gal"]=gall
    
    proid=dashboard.objects.filter(us_id=request.user.id)
    if len(proid)>0:
        entry=dashboard.objects.get(us_id=request.user.id)
        dis['disent']=entry
    return render (request,"prof.html",dis)

def updateprofile(request):
    dis={}
    proid=dashboard.objects.filter(us_id=request.user.id)
    if len(proid)>0:
        entry=dashboard.objects.get(us_id=request.user.id)
        dis['disent']=entry
        if request.method=="POST":
            frn=request.POST["frn"]
            lan=request.POST["lan"]             
            em=request.POST["em"]
            con=request.POST["con"] 
            add=request.POST["add"]
            city=request.POST["city"]
            usr=User.objects.get(id=request.user.id)
            usr.first_name=frn
            usr.last_name=lan
            usr.email=em
            usr.save()
            entry.contactno=con
            entry.address=add
            entry.city=city
            entry.save()
            if "pimg" in request.FILES:
                pro_image=request.FILES["pimg"]
                entry.profilepic=pro_image
                entry.save()
    return render (request,"updateprofile.html",dis)
    