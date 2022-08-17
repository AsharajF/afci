from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class dashboard(models.Model):
    us=models.ForeignKey(User,on_delete=models.CASCADE)
   
    profilepic=models.ImageField(upload_to="media/profileimages", default='default.jpg')
    contactno=models.BigIntegerField(default='1000000000')
    city=models.CharField(max_length=25,blank=True)
    address=models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    regno=models.IntegerField(default='1234')
    courseopt=models.CharField(max_length=50,blank=True)
    position=models.CharField(max_length=30,default="Student")
    is_rec=models.BooleanField(default=False)
    is_test=models.BooleanField(default=False)
    is_live=models.BooleanField(default=False)
    des=models.TextField(max_length=500,null =True)

    def __str__(self) -> str:
        return self.us.username

class apply_afci(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    profilepic=models.ImageField(upload_to="media/profileimages", default='default/profile.jpg')
    contactno=models.BigIntegerField(default='1000000000')
    city=models.CharField(max_length=25,blank=True)
    quali=models.CharField(max_length=25,blank=True)
    workex=models.CharField(max_length=25,blank=True)
    gender=models.CharField(max_length=30,blank=True)
    cv=models.FileField(upload_to="cv")
    applyfor=models.CharField(max_length=60)




    