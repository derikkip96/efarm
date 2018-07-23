from django.contrib import admin

# Register your models here.
from book.models import Hire


class HireAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email',
					'address', 'postal_code', 'city', 'paid',
					'created', 'updated']
	list_filter = ['paid', 'created', 'updated']
admin.site.register(Hire, HireAdmin)
