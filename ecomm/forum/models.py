from datetime import timezone, datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import now as timezone_now
import os

# Create your models here.
def upload(instance,filename):
    now=timezone_now()
    filename_base,filename_ext=os.path.splitext(filename)
    return 'quotes {}{}'.format(now.strftime("%Y/%m/%Y%m%d%H%M%S"),filename_ext.lower())

class Post(models.Model):
    title=models.CharField(max_length=250, db_index=True)
    image = models.ImageField(upload_to=upload, blank=True)
    Description=models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

    @property
    def get_content_type(self):
        content_type= ContentType.objects.get_for_model(Post)
        return content_type


    class Meta:
        ordering=('-date',)
        index_together=(('id','title'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', args=[self.id ])
    def get_post_like_url(self):
        return reverse('postlike',args=[self.id])

class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    ask_question =models.TextField()
    asked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('asked',)
        get_latest_by ='asked'

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return  reverse('question',args=[self.id])




class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    date =models.DateTimeField(auto_now_add=True)
    text = models.TextField()

