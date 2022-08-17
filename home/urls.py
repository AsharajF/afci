from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    
path("",views.myname,name="hm"),
path('abt',views.about,name="about"),
path('cour/<int:cid>',views.courses,name="courses"),
path('crs',views.cours,name="crs"),
path("search",views.search, name='search'),
path("cart", views.cartn, name="cart"),
path("live",views.live,name="live"), 
path("lect", views.lect, name="lect"),
path("test",views.test,name="test"),
path("material", views.material, name="material"),
path("rcart",views.rcart,name="rcart"),
path("get_cart_data",views.get_cart_data,name="get_cart_data"),
path("contact",views.contact,name="contact"),
path(" propmt",views.process_payment,name="process_payment"),
path("pmtdn",views.payment_done,name="payment_done"),
path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
path("add_recor",views.add_recor,name="add_recor"),
path("add_liv",views.add_liv,name="add_liv"),
path("add_tests",views.add_tests,name="add_tests"),
path("crs/<int:cid>" ,views.crsdet,name="crs"),
path("cour/crs/<int:cid>" ,views.crsdet,name="crs"),
path("fd",views.Feedback,name="fd"),
path("tech",views.teacher,name="tech"),
path("director",views.director,name="director"),
path("Placement",views.Placement,name="Placement"),
path("Gallery",views.Gallery,name="Gallery"),
path("Subs_email",views.Subs_email,name="Subs_email"),
path("faq",views.faq,name="faq"),
path("privacy",views.privacy,name="privacy"),
path("termsandconditions",views.terms_conditions,name="termsandconditions")
]

