from django.db import models
from datetime import datetime
from userinfo.models import UserInfo
# Create your models here.


class ArticleCategory(models.Model):
    category_id = models.IntegerField(auto_created=True, primary_key=True)
    category_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.category_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    createtime = models.DateTimeField(default=datetime.now())
    lastmodifytime = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    isdraft = models.BooleanField(default=False)
    viewnum = models.IntegerField(default=0)
    favor = models.IntegerField(default=0)
    Category = models.ForeignKey(ArticleCategory)
    user = models.ForeignKey(UserInfo)


class Comment(models.Model):
    review = models.TextField()
    user = models.ForeignKey(UserInfo)
    favor = models.IntegerField(default=0)
    article = models.ForeignKey(Article)