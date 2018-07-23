from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from  cabook.booky import Book
from .forms import BookForm
from .models import HiredItem

from hire.models import Input

@login_required(login_url='logint')
def BookView(request):
    booky=Book(request)
    if request.method=='POST':
        b_form=BookForm(request.POST)
        if b_form.is_valid() and request.user.is_authenticated:
            hire=b_form.save()
            for item in booky:
                HiredItem.objects.create(
                    hire=hire,
                    input=item['input'],
                    price=item['price'],

                )
            booky.clear()
            subject="Book id {}".format(hire.id)
            message="Dear {}, \n\n you have successful booked an item for hire. " \
                    "\nWe will look at your booking and get back to you in two weeks time ".format(hire.first_name)

            send_mail(subject,message,settings.EMAIL_HOST_USER,[hire.email],fail_silently=True)


            return redirect('hire_list')
    else:
        b_form=BookForm(instance=request.user)
    return render(request,'shop/book/book_create.html',{'b_form':b_form})
