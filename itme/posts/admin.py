from django.contrib import admin
from .models import Posts
# Register your models here.
class postmodeladmin(admin.ModelAdmin):
    list_display = ["title","timestamp","updatestamp"] #there are many adminmodels variables to customize,check docs
    search_fields = ["title","content"]
    class Meta:
        model = Posts
admin.site.register(Posts,postmodeladmin)
