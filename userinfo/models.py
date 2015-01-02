from django.db import models
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import ModelForm

oauth = (
    (0, 'Tencent'),
    (1, 'Weibo'),
    (2, 'RenRen'),
)


class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    nickname = models.CharField(max_length=50, blank=True)
    oauth_type = models.CharField(max_length=50, choices=oauth, blank=True)
    token = models.CharField(max_length=1000, blank=True)
    refrush = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('user','nickname',)