from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
