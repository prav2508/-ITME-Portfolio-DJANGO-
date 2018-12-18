from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from .forms import Login_form,Register_form,Profile_update_form
from django.contrib.auth import (
login,
logout,
authenticate,
get_user_model,
)
from .models import UserProfile
from django.urls import reverse

def Signin_view(request):
    form = Login_form()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user,backend=None)
            print("logged in")
            return redirect("mainprofile")
            #return reverse('mainprofile')
        else:
            return HttpResponse("<h1>fail</h1>")
    context = {
    "forms":form
    }
    return render(request,"signin.html",context)

def Signout_view(request):
    logout(request)
    print("logged out")
    context = {
    }
    return HttpResponse("<h1>signed out</h1>")

def Register_view(request):
    form = Register_form()
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            User = form.save()
            password = form.cleaned_data.get("password")
            User.set_password(password)
            User.save()
            return redirect("/accounts/signin/")

    context = {
        'forms':form
    }
    return render(request,"Signup.html",context)
def Profile_update(request):
    uid=request.user.id
    instance = UserProfile.objects.get(id=uid)
    form = Profile_update_form(instance=instance)
    if request.method == 'POST':
        form = Profile_update_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/accounts/userprofile")
    context = {
    "instance": instance,
    "forms":form,
            }
    return render(request, "UserProfile_update.html", context)
