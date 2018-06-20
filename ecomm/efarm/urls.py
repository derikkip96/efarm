from django.urls import path,re_path
from . import views
from django.conf.urls import url




urlpatterns =[
				url(r'^ecom/', views.product_list, name='product_list'),
				url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
				url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),

]
