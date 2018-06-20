from django.contrib import admin
from . models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','body','created']
    list_filter = ['created','active']
admin.site.register(Comment,CommentAdmin)

# Register your models here.
