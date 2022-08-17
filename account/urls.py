from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    path('', views.register, name='register'),
    #path('treg', views.stregister, name='treg'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='signout'),
    path('uprofile',views.updateprofile, name='uprofile'),
    path('dashboard',views.profile, name='dashboard'),
    path('Apply_afci', views.Apply_afci, name='Apply_afci'),
    
]