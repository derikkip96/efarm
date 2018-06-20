from celery import task
from celery.decorators import task
from django.core.mail import send_mail
from . models import Order

@task
def order_created(order_id):
	# task to send email notification after successful order
	order = Order.objects.get(id=order_id)
	subject = 'Order nr.{}'.format(order.id)
	message = 'Dear {} ,\n\n you have successful placed an order Your order id is {}.'.format(order.first_name,
																								 order.id)
	mail_sent = send_mail(
							subject,
							message,
							'dembakip@gmail.com',
							[order.email]
							)
	return mail_sent