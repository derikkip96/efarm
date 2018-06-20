from django.shortcuts import render, get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO

def show_me_the_money(sender,request, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        # mark the order as paid
        order.paid = True
        order.save()
        # create invoice

        subject ='efarm - invoice_no {}'.format(order.id)
        message ='please find attached invoice for your recent purchases'
        email = EmailMessage(subject,
                             message,
                             'dekiprotich@gmail.com',
                             [order.email])
        # generate pdfs
        html = render_to_string('orders/order/pdf.html',{'order':order})
        out = BytesIO()
        stylesheets = [weasyprint.CSS(settings.STATIC_ROOT +'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
        # attach the pdfs
        email.attach('order{}.pdf'.format(order.id),
                     out.getvalue(),
                     'application/pdf')
        # send mail
        email.send()

		
        if ipn_obj.receiver_email != "dekiprotich@gmail.com":
            # Not a valid payment
            return render(request,'payment/error.html')
valid_ipn_received.connect(show_me_the_money)