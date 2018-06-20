from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

def export_to_csv(ModelAdmin,request,queryset):
	opts = ModelAdmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['content-Disposition'] = 'attachment; filename ={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)
	fields  =[field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# first row with header information
	writer.writerow([field.verbose_name for field in fields])
	# write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_description = 'Export_to_CSV'
def admin_order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(reverse("order_detail",args=[obj.id])))
admin_order_detail.allow_tags = True
def order_pdf(obj):
	return mark_safe('<a href="{}">PDF</a>'.format(reverse('order_pdf',args=[obj.id])))
order_pdf.allow_tags = True
order_pdf.short_description ='BILL pdf'
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email',
					'address', 'postal_code', 'city', 'paid',
					'created', 'updated', admin_order_detail,order_pdf]
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]
	actions =[export_to_csv]
admin.site.register(Order, OrderAdmin)
