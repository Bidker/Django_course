from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf, request


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def loggedin(request):
    return render(request, 'loggedin.html', {'user_name' : request.user.username })


def invalid_login(request):
    return render(request, 'invalid_login.html')