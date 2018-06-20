from django.contrib import admin
from . models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display=['name','location','created','updated','price','image','stock','available']
	list_filter =['created','available','updated']
	list_editable=['available','stock','price']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)
