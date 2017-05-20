from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Notifications

def show_notification(request, pk):
    n = Notifications.objcets.get(pk=pk)
    return render(request, 'notification.html', { 'notification' : n })

def delete_notification(request, pk):
    n = Notifications.objcets.get(pk=pk)
    n.viewed = True
    n.save
    
    return HttpResponseRedirect('/accounts/loggedin')