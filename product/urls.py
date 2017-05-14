from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^login/$', views.user_login, name='user_login'),
    url(r'^$', views.product_list, name='product_list'),
    # url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^like/$', views.product_like, name='like'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
