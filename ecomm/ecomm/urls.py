"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import url,include

urlpatterns = [
    path(r'admin/',admin.site.urls),
    path(r'cart/',include('cart.urls')),
    path(r'orders/', include('orders.urls')),    
    path(r'coupons/',include('coupons.urls')),
    path(r'paypal/', include('paypal.standard.ipn.urls')),
    path(r'payment/', include('payment.urls')),
    path(r'account/', include('account.urls')),
    path(r'forum/',include('forum.urls')),
    path(r'hire/',include('hire.urls')),
    path(r'efarm/', include('efarm.urls')),
    path(r'search/', include('haystack.urls')),
    # path('', include('social.apps.django_app.urls', namespace='social')),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
