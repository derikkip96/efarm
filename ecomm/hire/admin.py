from django.contrib import admin
from . models import Category,Input

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
class InputAdmin(admin.ModelAdmin):
    list_display = ['name','location','created','updated','price','image','available']
    list_filter = ['created','updated','available']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Input,InputAdmin)

