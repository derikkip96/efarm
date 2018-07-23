from django.contrib.auth.models import User
from django.db import models
from hire.models import Input

# Create your models here.
class Hire(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField()
    address= models.CharField(max_length=50)
    email= models.EmailField()
    postal_code=models.CharField(max_length=20)
    city =models.CharField(max_length=25)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    hired =models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering=('-updated',)

    def __str__(self):
        return 'hire {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())

class HiredItem(models.Model):
    hire=models.ForeignKey(Hire, on_delete=models.CASCADE,related_name='items')
    input=models.ForeignKey(Input, on_delete=models.CASCADE,related_name='hired_items')
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def _str_(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price*self.quantity
