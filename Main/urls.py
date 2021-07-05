from django.urls import path
from Main import views

urlpatterns = [  
    path('', views.index, name="Home"),  
    path('aboutus', views.aboutus, name="About us"),
    path('contact', views.contact, name="Contact"),
    path('newproduct', views.newproduct, name="New product"),
    
]