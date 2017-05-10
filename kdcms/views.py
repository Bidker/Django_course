from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf, request


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def logout(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def loggedin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def invalid(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)