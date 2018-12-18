from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from posts.models import Posts
from accounts.models import UserProfile
from .forms import Create_post_form
# Create your views here.
class Create_post(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = Create_post_form()
            context ={
            'forms':form
            }
            return render(request,"create_post.html",context)
        else:
            return HttpResponse("<h1>sign in to view</h1>")
    def post(self,request):
        if request.user.is_authenticated:
            form = Create_post_form(request.POST,request.FILES)
            if form.is_valid():
                #user =request.user
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()

                context ={
                'forms':form
                }
            return render(request,"create_post.html",context)
        else:
            return HttpResponse("<h1>sign in to view</h1>")

class Wall_view(View):
    def get(self,request):
        if request.user.is_authenticated:

            user = request.user

            queryset = Posts.objects.filter(user_id=user.id).order_by("-timestamp")
            userprof = UserProfile.objects.get(id=user.id)
            sharelink = "http://localhost:8000/posts/"+str(user.id)+"/"
            context = {
            "objt" : queryset,
            "user_ob" : userprof,
            "user" : user,
            "sharelink":sharelink
            }
            return render(request,"post_list.html",context)
        else:
            return HttpResponse("<h1>sign in to view</h1>")
class Share_view(View):
    def get(self,request,id):
        queryset = Posts.objects.filter(user_id=id).order_by("-timestamp")
        userprof = UserProfile.objects.get(id=id)
        context = {
        "objt" : queryset,
        "user_ob" : userprof,
        }
        return render(request,"share_posts_list.html",context)
