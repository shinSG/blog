from django.contrib import admin
from userinfo.models import UserInfo

# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['nickname']

admin.site.register(UserInfo, UserInfoAdmin)

