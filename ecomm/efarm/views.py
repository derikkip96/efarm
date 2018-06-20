from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from cart.forms import shoping
from django.contrib import messages
from haystack.query import SearchQuerySet
import json


def product_list(request ,category_slug=None):
	storage =messages.get_messages(request)
	category = None
	categories= Category.objects.all()
	products=Product.objects.filter(available=True)
	# adding up shopping cart form
	cart_form=shoping()
	# adding pagination to product list
	prod_list=Product.objects.all()
	paginator =Paginator(prod_list,50)
	page = request.GET.get('page')
	try:
		products= paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter( category=category )
	return render(request,'shop/product/product.html', {'category':category,
														'categories':categories,
														'products':products,
														'page':page,
														'cart_form':cart_form,
														'message':storage}
														)
def product_detail(request, id, slug):
	product=get_object_or_404(Product,
								id=id,
								slug=slug,
								available=True
								)
	cart_form = shoping()
	return render(request, 'shop/product/detail.html',{'product':product,'cart_form':cart_form})
def autocomplete(request):
	products=SearchQuerySet.autocomplete(content_auto = request.GET.get('q',''))
	suggestions = [result.name for result in products]
	the_data= json.dumps({
		'result':suggestions
	})

	return HttpResponse(the_data, content_type='application/json')

