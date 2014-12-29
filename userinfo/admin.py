from django.contrib import admin
from userinfo.models import userinfo

# Register your models here.

class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['nickname']

admin.site.register(userinfo, UserinfoAdmin)

