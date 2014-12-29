from django.db import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.forms import ModelForm

oauth = (
    (0, 'Tencent'),
    (1, 'Weibo'),
    (2, 'RenRen'),
)


class userinfo(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    nickname = models.CharField(max_length=50, unique=True, blank=False)
    oauth_type = models.CharField(max_length=50, choices=oauth, blank=True)
    token = models.CharField(max_length=1000, blank=True)
    refrush = models.IntegerField(blank=True)


class userform(ModelForm):
    class Meta:
        model = userinfo
        fields = ('user','nickname',)