from django.conf.urls import url
from . import views
from django.contrib.auth.views import *
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^$', views.product_list, name='product_list'),
    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # url(r'^login/$', views.user_login, name='user_login'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='    product_detail'),
]
