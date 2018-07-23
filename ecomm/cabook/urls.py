from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^book/detail/$', views.book_detail, name='bookdetail'),
    url(r'^book/(?P<input_id>\d+)/$', views.add_book_item, name='hire'),
    url(r'^cancel/(?P<input_id>\d+)/$', views.remove_book, name='cancel_book')
]