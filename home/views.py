from email import message
import email
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from decimal import Decimal
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse,JsonResponse
from .models import Courses, exdb, Videolecture, branch , cart, offers, placement , studymaterial, Contact ,Order, Live, feedback, Test, timetable , gallery,subs_email
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from account.models import*
import datetime
# Create your views here
def myname(request):
    dic={}
    notic=timetable.objects.all()
    materials=studymaterial.objects.all()
    stfpro= dashboard.objects.all()
    
    new_s=offers.objects.all()
    cr=branch.objects.all()
    crr=Courses.objects.all()
    gall=gallery.objects.all()
    proid=exdb.objects.filter(user_id=request.user.id)
    if len(proid)>0:
        ev=exdb.objects.get(user_id=request.user.id)
        dic["ev"]=ev

    dic["gal"]=gall
    dic['noti']=notic
    dic['news']=new_s
    dic['stu']=materials
    dic['stf']=stfpro
    dic['cro']=crr
    dic['key']=cr
    return render(request,"index-1.html",dic)
    

def about(request):
    dic={}
    cr=branch.objects.all()
    dic['cro']=cr
    return render(request,"about.html",dic)


def courses(request,cid):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    brn=branch.objects.get(id=cid)
    cr=Courses.objects.filter(bran=brn).order_by("id")
    dic["cro"]=cr
    return render(request,"course.html",dic)

def cours(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    cr=Courses.objects.all().order_by("bran")
    dic["cro"]=cr
    return render(request,"course.html",dic)
    
def search(request):
    dic={}
    if request.method=='GET':
        sr=request.GET["search"]
        xyz=Courses.objects.filter(name__icontains=sr)
        dic['cro']=xyz
    return render (request,"course.html",dic)            
            
def cartn(request):
    item= cart.objects.filter(user_id=request.user.id,status=False)
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    dic["item"]=item
    if request.user.is_authenticated:
        if request.method=="POST":
            cartid=request.POST["ct"]
            quantity=request.POST["qty"]
            price=request.POST["fee"]
            is_exist=cart.objects.filter(crs_id=cartid, user_id=request.user.id, status=False)
            if len(is_exist)>0:
                dic["msg"]="This course already exists"
                dic["cls"]="alert alert-warning"
            else:
                cor=get_object_or_404(Courses,id=cartid) #same as get
                usr=get_object_or_404(User,id=request.user.id)

                crt=cart(user=usr,crs=cor,quantity=quantity,fees=price)
                crt.save()
                dic["msg"]="{} Course added to cart".format(cor.name)
                dic["cls"]="alert alert-success"


    return render (request,"cart.html",dic)

def rcart(request):
    if "delete_cart" in request.GET:
        id=request.GET['delete_cart']
        crtobj=get_object_or_404(cart,id=id)
        crtobj.delete()
    return HttpResponse(1)


def get_cart_data(request):
    item = cart.objects.filter(user__id=request.user.id, status=False)
    sale, quantity = 0,0
    for i in item:
        sale += float(i.fees)*i.quantity
        quantity = quantity+int(i.quantity)
        ds=sale*10/100
        gt=sale-ds
        resp = {"quan": quantity, "tot": sale,"dis":ds,"gt":gt}
    return JsonResponse(resp)

def lect(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    cr=Videolecture.objects.all()
    dic["cro"]=cr
    return render(request,"recorded.html",dic)

def live(request):
    dic={}
    cr=Live.objects.all()
    gall=gallery.objects.all()
    dic["gal"]=gall
    dic["cro"]=cr
    return render(request,"live.html",dic)   

def test(request):
    dic={}
    cr=Test.objects.all()
    gall=gallery.objects.all()
    dic["gal"]=gall
    dic["cro"]=cr
    return render(request,"test.html",dic) 

def material(request):
    dic={}
    mat=studymaterial.objects.all()
    gall=gallery.objects.all()
    dic["gal"]=gall
    dic["cro"]=mat

    return render(request,"study_materials.html",dic) 

def contact(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        msg=request.POST['msg']
        if len(name)<2 or len(email)<3 or len(msg)<4:
            message.error(request, "Please fill the form correctly")
        else:
            con=Contact(name=name, email=email, phone=phone, msg=msg)
            con.save()
            
    return render(request,"contact.html",dic)
def process_payment(request):
    item = cart.objects.filter(user_id=request.user.id,status=False)
    products=""
    amt=0
    inv="AFCI01inv0"
    cart_ids=""
    p_ids=""
    for i in item:
        products+=str(i.crs.name)+"\n"
        p_ids+=str(i.crs.id)+","
        amt+=float(i.crs.fees)/77
        inv=str(i.id)
        cart_ids=str(i.id)

   

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': amt,
        'item_name': products,
        "invoice":inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,products_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()      
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def add_recor(request):
    dic={}
    gall=gallery.objects.all()
    crs=Courses.objects.all()
    dic["gal"]=gall
    dic["crs"]=crs
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=='POST':
        crs=request.POST['crs']
        vname=request.POST['vname']
        descrip=request.POST['descrip']
        cro=get_object_or_404(Courses,id=crs)
        vid=Videolecture(teacher=usr,c_ourse=cro,vidname=vname,description=descrip)
        vid.save()
        if "rec_lec" in request.FILES:
                rec=request.FILES["rec_lec"]
                vid.lecture=rec
                vid.save()
    return render(request,"add_rec.html",dic)

def add_liv(request):
    dic={}
    gall=gallery.objects.all()
    crs=Courses.objects.all()
    dic["gal"]=gall
    dic["crs"]=crs
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=='POST':
        crs=request.POST['crs']
        tname=request.POST['tname']
        schedu=request.POST['sched']
        link=request.POST['up_link']
        cro=get_object_or_404(Courses,id=crs)
        liv=Live(teacher=usr,c_ourse=cro,Topic=tname,scheduled=schedu,link=link)
        liv.save()
        
    return render(request,"add_live.html",dic)

def add_tests(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    crs=Courses.objects.all()
    dic["crs"]=crs
    usr=get_object_or_404(User,id=request.user.id)
    if request.method=='POST':
        crs=request.POST['crs']
        tname=request.POST['tname']
        schedu=request.POST['sched']
        cro=get_object_or_404(Courses,id=crs)
        liv=Test(teacher=usr,c_ourse=cro,Topic=tname,scheduled=schedu)
        liv.save()
        if "up_link" in request.FILES:
                li=request.FILES["up_link"]
                liv.link=li
                liv.save()
    return render(request,"add_test.html",dic)


def staff(request): 
    dic={}
    gall=gallery.objects.all()
   #for individual page
    stfpro= dashboard.objects.all()
    
    return render(request,"index-1.html",{"stf":stfpro},{"gal":gall})
    


def crsdet(request,cid):
    dic={}
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    var=Courses.objects.get(id=cid)
    feeds=feedback.objects.filter(crs=cid)
    dic['feed']=feeds
    dic["crs"]=var

    return render(request,"course-details.html",dic)

def Feedback(request):
    dic={}
    
    usr=get_object_or_404(User,id=request.user.id)
    prf=dashboard.objects.get(us_id=request.user.id)
    
    if request.user.is_authenticated:
        if request.method=='POST':
            brid=request.POST['brid']
            mes=request.POST['comments']
            rate=request.POST['rat']
            em=request.POST['email']
            br=get_object_or_404(Courses,id=brid)
            fdcr=feedback(user=usr,prf=prf,crs=br,msg=mes,rating=rate)
            fdcr.save()
            return redirect('hm')

        
    return render(request,"course-details.html")
def teacher(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    tech=dashboard.objects.all()
    dic["tec"]=tech
    return render(request,"teacher.html",dic)

def director(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    return render(request,"director.html",dic)

def Placement(request):
    if request.method=='POST':
        name=request.POST['name']
        num=request.POST['nbm']
        wnum=request.POST['wnbm']
        qual=request.POST['qualification']
        wrkex=request.POST['workex']
        email=request.POST['email']
        address=request.POST['address']
        dob=request.POST['dob']
        interest=request.POST['area']


        placem=placement(name=name,number=num, wnumber=wnum, quali=qual , work_ex=wrkex,email=email,address=address, dob=dob, interest=interest)
        placem.save()
        return redirect('about')

    return render(request,"placement.html")

def Gallery(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    return render(request,"index-1.html",dic)

def Subs_email(request):
    if request.method=='POST':
        em=request.POST['course']
        e_mail=subs_email(email=em)
        e_mail.save()
        return redirect('hm')
    return render(request,"index-1.html")

def faq(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    return render(request,"faq.html",dic)

def privacy(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    return render(request,"Privacy Policy.html",dic)

def terms_conditions(request):
    dic={}
    gall=gallery.objects.all()
    dic["gal"]=gall
    return render(request,"Terms and Conditions.html",dic)
