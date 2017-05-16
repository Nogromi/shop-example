from django.conf.urls import url
from . import views
from django.conf.urls import url, include
from django.contrib.auth.views import *
urlpatterns = [

    url(r'^register/$', views.register, name='register'),

    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),


    url(r'^$', views.product_list, name='product_list'),
    # url(r'^da'shboard/$', views.dashboard, name='dashboard'),

    url(r'^like/$', views.product_like, name='like'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
