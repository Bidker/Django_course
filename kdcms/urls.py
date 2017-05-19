"""kdcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from articles import urls
from kdcms import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'article/', include('articles.urls')),
    url(r'accounts/', include('userprofile.urls')),
    url(r'notifications/', include('notifications.urls')),
    
    url(r'^accounts/login/$', views.login, name = 'login'),
    url(r'^accounts/auth/$', views.auth_view, name = 'auth_view'),
    url(r'^accounts/logout/$', views.logout, name = 'logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name = 'loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name = 'invalid_login'),
   
    url(r'^accounts/create_user/$', views.create_user, name = 'create_user'),
    url(r'^accounts/create_user_success/$', views.create_user_success, name = 'create_user_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)