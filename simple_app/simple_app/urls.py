"""simple_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.contrib.auth import views as auth_views
from simple_app.views import IndexView, SignedInIndexView

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^js/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.STATIC_ROOT,'js')}),
    url(r'^css/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.STATIC_ROOT,'css')}),
    url(r'^img/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.STATIC_ROOT,'img')}),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^userhome$', SignedInIndexView.as_view(), name="index_signedin"),
    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view()),
]
