from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^write/$', views.write, name='write'),
    url(r'^$', views.allPosts, name='allPosts'),
    url(r'^detail/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^likes/(?P<post_id>\d+)/$', views.likes, name='likes'),
    url(r'^subject/(?P<subject_id>\d+)$', views.sortedPosts, name='sortedPost'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^signup/$', views.signup, name='signup'),
    url('^', include('django.contrib.auth.urls')),
]