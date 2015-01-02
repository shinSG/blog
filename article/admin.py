from django.contrib import admin
from article.models import ArticleCategory, Article, Comment

# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']


admin.site.register(ArticleCategory,ArticleCategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'createtime', 'author', 'favor', 'viewnum']
    #list_filter = ['author']

    def author(self, obj):
        return u'%s' % obj.user.user.username

admin.site.register(Article,ArticleAdmin)