from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
def upload_location(instance, filename):

    #filebase, extension = filename.split(".")

    #return "%s/%s.%s" %(instance.id, instance.id, extension)

    return "media/accounts/%s/%s" %(instance.id, filename)
class UserProfile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    #other fields here
    name = models.CharField(max_length=100,default=None,blank=True,null=True)
    profile_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")

    height_field = 180

    width_field = 171#models.IntegerField(default=0)

    place =models.CharField(max_length=100,default='India,banglore',blank=True,null=True)

    profession = models.CharField(max_length=100,default=None,blank=True,null=True)

    contact_number = models.CharField(max_length=100,default=None,blank=True,null=True)



    def __str__(self):
          return "%s's profile" % self.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(username=instance)

post_save.connect(create_user_profile, sender=User)
