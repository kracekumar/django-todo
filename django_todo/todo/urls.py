# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import ProfileView, auth_success
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^complete/github/$', auth_success, name='auth_sucess'),
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
)
