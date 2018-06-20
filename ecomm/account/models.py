from django.db import models
from django.conf import settings
from django.utils.timezone import now as timezone_now
import os

# Create your models here.
def upload(instance,filename):
	now =timezone_now()
	filename_base,filename_ext=os.path.splitext(filename)
	return 'user {}{}'.format(now.strftime("%Y/%m/%Y%m%d%H%M%S"), filename_ext.lower())
class Profile(models.Model):
	user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	image = models.ImageField(upload_to='upload', blank=True)

	def __str__(self):
		return 'profile for{}'.format(self.user.username)
