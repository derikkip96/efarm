from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from . forms import OrderForm
from . models import  OrderItem
from . models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from cart.cart import Cart
from .tasks import order_created
@login_required(login_url='logint')
def orderView(request):
	cart = Cart(request)
	if request.method =='POST':
		order_form = OrderForm(request.POST)
		if order_form.is_valid() and request.user.is_authenticated:
			order=order_form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
										 product=item['product'],
										 price=item['price'],
										 quantity=item['quantity'] )
			# set empty cart
			cart.clear()
			# assynchronous task
			order_created.delay(order.id)
			# getting order id and setting it in the session
			request.session['order_id']= order.id
			return redirect(reverse('process'))
	else:
		order_form = OrderForm(instance=request.user)
	return render(request,'orders/order/create.html',{'cart':cart,'order_form':order_form})
@staff_member_required
def order_detail(request,order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'Admin/orders/order/details.html',{'order':order})
@staff_member_required
def print_pdf(request,order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html',{'order':order})
	response = HttpResponse(content_type='application/pdf')
	response ['context-Disposition'] = 'filename =\ "order_{}.pdf"'.format(order.id)
	weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])
	return response