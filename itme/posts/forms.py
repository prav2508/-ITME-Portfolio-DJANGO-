from django import forms
from posts.models import Posts


class Create_post_form(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = [
        'title',
        'post_image',
        'description'
        ]
