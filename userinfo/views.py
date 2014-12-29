from django.shortcuts import render_to_response
#from django.http.response import HttpResponse
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_protect
from userinfo.models import userinfo, userform
from django.contrib.auth.models import User
# Create your views here.
def submitregister(request):
    if request.method == "GET":
        return HttpResponse({'error': 'Forbidden'})
    userform = request.POST
    print userform
    user_a = User()
    user_a.username = userform['user_username']
    user_a.password = userform['user_password']
    user_a.email = userform['user_email']
    f = userinfo()
    print '***'
    user_a.save()
    print '@@@@@'
    f.user = User.objects.get(username=user_a.username)
    print '$$$$'
    f.save()



@csrf_protect
def register(request):
    usr = userinfo()
    form = userform()
    return render_to_response("registerpage.html", RequestContext(request, {'form': form}))
    #return HttpResponse(loader.get_template("registerpage.html").render(c))

