import re
from django.shortcuts import render_to_response
#from django.http.response import HttpResponse
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_protect
from userinfo.models import UserInfo, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.


@csrf_protect
def submitregister(request):
    if request.method == "GET":
        return HttpResponse({'error': 'Forbidden'})
    userform = request.POST
    print userform
    user_a = User()
    user_a.username = userform['user_username']
    user_a.password = make_password(userform['user_password'])
    user_a.email = userform['user_email']
    f = UserInfo()
    user_a.save()
    f.user = User.objects.get(username=user_a.username)
    f.save()
    return render_to_response('registersuccess.html', {'info': 'Regist SUCCESS!'})



@csrf_protect
def register(request):
    usr = UserInfo()
    form = UserForm()
    return render_to_response("registerpage.html", RequestContext(request, {'form': form}))
    #return HttpResponse(loader.get_template("registerpage.html").render(c))

