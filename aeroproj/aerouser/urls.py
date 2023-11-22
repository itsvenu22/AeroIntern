from django.urls import path

from . import views

urlpatterns = [
    path("login", views.index, name="login"),
    path("signup",views.home_view, name="signup" ),
    #path("details/<int:id>", views.details, name='details'),
]
