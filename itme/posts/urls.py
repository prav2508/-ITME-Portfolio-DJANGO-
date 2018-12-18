from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import Create_post,Wall_view,Share_view
urlpatterns = [
    #path('xyz/',TemplateView.as_view(template_name="base1.html")),
    path('main_wall/',Wall_view.as_view(),name="mainprofile"),
    path('create_post/',Create_post.as_view(),name="addpost"),
    path('<int:id>/',Share_view.as_view(),name="viewpost")
]
