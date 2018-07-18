from django.contrib import admin
from .models import Post,Question,Answer

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','image','date']
    list_filter = ['date',]
admin.site.register(Post,PostAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display =['user','ask_question']
    list_filter = ['asked']
admin.site.register(Question,QuestionAdmin)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'body','date']
    list_filter = ['date']
admin.site.register(Answer,AnswerAdmin)