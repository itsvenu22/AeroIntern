from django.urls import path
from . import views

urlpatterns = [
    path("devicereg", views.devicereg, name="devicereg"), 
    path("patientreg", views.patientreg, name="patientreg"),  
    path("patients", views.patients, name="patients"),  
    path("mylog", views.mylog, name="mylog"),  
    path("alldevices", views.alldevices, name="alldevices"), 
    path("otherlog",views.otherlog, name="otherlog"),
]
