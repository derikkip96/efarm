from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.views.decorators.http import require_POST
from .booky import Book
# from .forms import HireForm
from hire.models import Input

# Create your views here.
# @require_POST
def add_book_item(request,input_id):
	book=Book(request)
	input=get_object_or_404(Input,id=input_id)
	book.add(input)
	return redirect('bookdetail')
def remove_book(request, input_id):
	book=Book(request)
	input=get_object_or_404(Input, id=input_id)
	book.remove(input)
	return redirect('bookdetail')
def book_detail(request):
	book=Book(request)
	return render(request,'shop/book/book_detail.html',{'book':book })