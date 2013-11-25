# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

#import todo
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'/logged-in', todo.views.logged_in, name="logged_in"),
    #url(r'/profile/$', todo.views.ProfileView.as_view(), name="profile"),
    url(r'', include('todo.urls')),
)
