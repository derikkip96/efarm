from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^bookingView/$',views.BookView, name='BookView')
]