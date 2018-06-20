import os

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.timezone import now as timezone_now


class Category(models.Model):
    name=models.CharField(max_length=250,db_index=True)
    slug=models.SlugField(db_index=True,unique=True)

    class Meta:
        ordering=('-name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('input_by_category',args=[self.slug])
def upload(instance,filename):
    now=timezone_now()
    filename_base,filename_ext=os.path.splitext(filename)
    return 'hire/%s%s' %(now.strftime("%Y/%m/%Y%m%d%H%M%S"),filename_ext.lower(),)

class Input(models.Model):
    name= models.CharField(max_length=250,db_index=True)
    slug=models.SlugField(db_index=True,unique=True)
    image=models.ImageField(upload_to=upload)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='inputs')
    price= models.DecimalField(max_digits=10, decimal_places=3)
    available=models.BooleanField(default=True)
    location=models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('input_detail', args=[self.id, self.slug])

