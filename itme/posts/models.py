from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
# Create your models here.
def upload_location(instance, filename):
    return "posts/%s/%s" %(instance.id, filename)
class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post_image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")

    height_field = models.IntegerField(default=0)

    width_field = models.IntegerField(default=0)
    description = models.TextField(max_length=200 )
    updatestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title
