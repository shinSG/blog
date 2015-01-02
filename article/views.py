from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.views.decorators.csrf import csrf_protect
from article.models import ArticleCategory, Article, Comment
# Create your views here.


@csrf_protect
def article(request):
    article = {
        'INFO': 'BAD REQUEST',
    }
    if request.method == 'GET':
        if request.GET.get('id'):
            articleid = request.GET.get('id')
            articleinfo = Article.objects.filter(id=articleid)
            if len(articleinfo) > 0:
                articleinfo = articleinfo[0]
                comments = []
                commentslist = Comment.objects.filter(article__id=articleid)
                for c in commentslist:
                    comments.append(c)
                article = {
                    'id': articleinfo.id,
                    'title': articleinfo.title,
                    'author': articleinfo.user.user.username,
                    'createtime': articleinfo.createtime.strftime("%Y-%m-%d %H:%M:%S"),
                    'content': articleinfo.content,
                    'view': articleinfo.viewnum,
                    'favor': articleinfo.favor,
                    'comments': comments
                }
    return render_to_response('article.html', Context({'article': article}))
