from django import forms
from django.contrib.auth import (
login,
logout,
authenticate,
get_user_model,
)
from .models import UserProfile
User = get_user_model()
class Login_form(forms.ModelForm):
    username = forms.CharField(max_length=100)
    #email = forms.EmailField(label="Email-Id",required=True)
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'username',
        'password'
        ]
#all about validation
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if username and password:
            if not len(password)>=5:
                raise forms.ValidationError("password must be more than 6 characters")
            if not user:
                raise forms.ValidationError("The user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("The user does not exist")
            if not user.is_active:
                raise forms.ValidationError("The user does not exist")

            return super(Login_form,self).clean(*args,**kwargs)
class Register_form(forms.ModelForm):
    email = forms.EmailField(label="Email-Id",required=True)
    password = forms.CharField(max_length=50,widget = forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",max_length=50,widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password',
        'password2'
        ]
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        username = self.cleaned_data.get("username")
        email_qs = User.objects.filter(email=email)
        un_qs = User.objects.filter(username=username)
        if email_qs.exists():
            raise forms.ValidationError("The email entered already exists ,pls sign in..")
        if email and password:
            if not len(password)>=8:
                raise forms.ValidationError("Password lenght must be more than 8")
        if un_qs.exists():
            raise forms.ValidationError("The user already exists...")

    def clean_password2(self,*args,**kwargs):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("The passwords dint match..")
class Profile_update_form(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = [
            'name',
            'profile_image',
            'place',
            'profession',
            'contact_number',
            ]
        #def clean_contact_number(self, *args,**kwargs):
            #cnum = self.cleaned_data.get("contact_number")
