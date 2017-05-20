from django.conf.urls import url
from notifications import views

urlpatterns = [
                      url(r'^show/(?P<pk>[0-9]+)/$', views.show_notification, name = 'show_notification'),
                      url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_notification, name = 'delete_notification'),
]