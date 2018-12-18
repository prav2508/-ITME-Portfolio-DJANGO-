from django.contrib import admin
from django.urls import path


from django.conf.urls import url

from django.views.generic import TemplateView
from accounts.views import (Signin_view,Signout_view,Register_view,Profile_update)

urlpatterns = [

    #path('signin/home/',TemplateView.as_view(template_name="home.html")),
    path('signin/',Signin_view,name = "signin"),
    path('signout/',Signout_view,name = "signout"),
    path('signup/',Register_view,name = "signout"),
    path('userprofile/',Profile_update,name="profileupdate")

]
