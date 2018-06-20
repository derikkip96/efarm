from django.conf.urls import url
from . import views

urlpatterns=[url(r'^orderView/$',views.orderView, name='orderView'),
				url(r'^Admin/order/(?P<order_id>\d+)/$',views.order_detail, name='order_detail'),
			 url(r'^Admin/order/(?P<order_id>\d+)/pdf/$',views.print_pdf,name='order_pdf')

				]