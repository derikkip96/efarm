from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.utils.html import format_html
from django.views.decorators.http import require_POST
from efarm.models import Product
from . forms import shoping
from .cart import Cart
from coupons.forms import CouponForm
from django.contrib import messages
from django.urls import reverse

def add_cart(request,product_id):
	cart = Cart(request)
	product = get_object_or_404(Product,id=product_id)
	form =shoping(request.POST)
	if form.is_valid():
		cd =form.cleaned_data
		cart.add(product =product,
					quantity=cd['quantity'],
					update_quantity=cd['update'])
		messages.info(request, '<button type="button"  class="close" data-dismiss="alert" aria-hidden="true">&times;</button>',extra_tags='safe')
		messages.info(request,'item has been added to you cart you may proceed and checkout')
		messages.info(request,'{} {} {}'.format('total:','Ksh',cart.get_the_total_cost()))
		msg = format_html('<button style="background-color:#00ff00;border:1px solid white;padding:5px;"><a style=" color:white;" href="{}">Checkout</a></button>',reverse('orderView' ))
		messages.info(request,msg)
	return redirect('product_list')
def remove_cart(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart_detail')
def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = shoping(initial={'quantity': item['quantity'],'update': True})
	coupon_apply_form = CouponForm()
	cart_products = [item['product'] for item in cart]

	return render(request,'shop/cart/cart_detail.html',{'cart':cart,
														'coupon_apply_form':coupon_apply_form }
														)
