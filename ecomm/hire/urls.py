from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input/$',views.hireView, name='hire_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.hireView, name='input_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.input_detail,name='input_detail'),

]