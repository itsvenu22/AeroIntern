from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    #path("details/<int:id>", views.details, name='details'),
]
