from django.conf.urls import url
from articles import views

urlpatterns = [
					  url(r'^show_all/$', views.articles, name = 'articles'),
					  url(r'^(?P<pk>[0-9]+)/$', views.article, name = 'article'),
					  url(r'^(?P<pk>[0-9]+)/add_comment/$', views.add_comment, name = 'add_comment'),
]