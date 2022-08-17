from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import *
from account.models import  dashboard
# Create your models here.
class branch(models.Model):
    branch_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    bimage=models.ImageField(upload_to='bracnchimg')
    added_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.branch_name


class Courses(models.Model):
    bran=models.ForeignKey(branch,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    duration=models.IntegerField()
    fees=models.IntegerField()
    fees2=models.IntegerField()
    fees3=models.IntegerField()
    cimage=models.ImageField(upload_to='courseimg')
    added_on=models.DateTimeField(auto_now_add=True)
    des=models.CharField(default=False,max_length=1500)
    def __str__(self):
        return self.name


class exdb(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    db=models.ForeignKey(dashboard,on_delete=models.CASCADE)
    crs=models.ManyToManyField(Courses,related_name="user")
    dur=models.CharField(default="1mth", max_length=200)
    is_status=models.BooleanField(default=False)
    def __str__(self):
        return self.db.us.username


    


class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    fees=models.IntegerField(default=0)
    crs=models.ForeignKey(Courses,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True)

class Videolecture(models.Model):
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)
    c_ourse=models.ForeignKey(Courses,on_delete=models.CASCADE)
    vidname=models.CharField(max_length=50)
    lecture=models.FileField(upload_to='videolectures')
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

class Live(models.Model):
    #bran=models.ForeignKey(branch,on_delete=models.CASCADE)
    c_ourse=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Topic=models.CharField(max_length=50)
    scheduled=models.DateTimeField(auto_now_add=True, null=True)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)
    link=models.URLField(max_length=200, null=True)

class Test(models.Model):
    c_ourse=models.ForeignKey(Courses,on_delete=models.CASCADE)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)
    Topic=models.CharField(max_length=50)
    scheduled=models.DateTimeField(auto_now_add=True, null=True)
    link=models.URLField(max_length=200, null=True)

class studymaterial(models.Model):
    bran=models.ForeignKey(branch,on_delete=models.CASCADE)
    matname=models.CharField(max_length=30)
    materials=models.FileField(upload_to='materials')
    added_on=models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    msg=models.TextField()
    time=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Message from' + ' ' + self.name + ' - ' + self.email

class Order(models.Model):
    cust_id=models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids=models.CharField(max_length=250)
    products_ids=models.CharField(max_length=250)
    invoice_id=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    processed_on=models.DateTimeField(auto_now_add=True)

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prf=models.ForeignKey(dashboard,on_delete=models.CASCADE)
    crs=models.ForeignKey(Courses,on_delete=models.CASCADE)
    rating=models.IntegerField()
    msg=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)
    
class offers(models.Model):
    nimg=models.ImageField(upload_to='not_img')
    added_on=models.DateField(auto_now_add=True)
    notice=models.CharField(max_length=250)

class timetable(models.Model):

    added_on=models.DateField(auto_now_add=True)
    topic=models.CharField(max_length=300)
    c_ourse=models.ForeignKey(Courses,on_delete=models.CASCADE)
    link=models.URLField(max_length=200, null=True)

class placement(models.Model):
    name=models.CharField(max_length=40)
    number=models.BigIntegerField()
    wnumber=models.BigIntegerField()
    quali=models.CharField(max_length=25,blank=True)
    work_ex=models.CharField(max_length=25,blank=True)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    dob=models.CharField(max_length=10)
    interest=models.CharField(max_length=50)

    def __str__(self):
        return 'Request from' + ' ' + self.name

class gallery(models.Model):
    img=models.ImageField(upload_to='Gallery')

class subs_email(models.Model):
    email=models.CharField(max_length=100)
    def __str__(self):
        return 'Subscribed Users:-' + ' ' + self.email



