from django.db import models
from django.urls import reverse
from django.utils.timezone import now as timezone_now

import os

#creating a category  table
class Category(models.Model):
	name = models.CharField(max_length=200 ,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True, unique=True)

	class Meta:
		ordering=('-name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name
	#absolute url for category
	def get_absolute_url(self):
		return reverse('product_list_by_category', args=[self.slug])
	#creating a table for products
def upload_to(instance,filename):
	now= timezone_now()
	filename_base, filename_ext = os.path.splitext(filename)
	return 'quotes/%s%s' %(now.strftime("%Y/%m/%Y%m%d%H%M%S"),filename_ext.lower(),
						   )
class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
	location =models.CharField(max_length=200)
	weigth = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to=upload_to, blank=True)
	available = models.BooleanField(default=True)
	stock = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
    
	class Meta:
		ordering=('-created',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('product_detail', args=[self.id, self.slug]
            )
	def save(self,*args,**kwargs):
		super(Product, self).save(*args,**kwargs)
		self.create_thumbnail()
	def create_thumbnail(self):
		from django.core.files.storage import default_storage as storage
		if not self.image:
			return ""
			file_path =self.image.name
			filename_base,filename_ext =os.path.splitext(file_path)
			thumbnail_file_path= "%s_thumbnail.jpg"% filename_base
			if storage.exists(thumbnail_file_path):
				return "exists"
		try:
			f=storage.open(file_path,'r')
			image=Image.open(f)
			width, height = image.size
			thumbnail_size= 50,50
			if width > height:
				delta = width - height
				left = int(delta/2)
				upper = 0
				right = height + left
				lower = height
			else:
				delta=height - width
				left = 0
				upper = int(delta/2)
				right = width
				lower = width + upper
			image =image.crop((left,upper,right,lower))
			f_mob= storage.open(thumbnail_file_path,"w")
			image.save(f_mob,"JPEG")
			f_mob.close()
			return "success"
		except:
			return "error"

	def get_thumbnail_picture_url(self):
		from PIL import Image
		from django.core.files.storage import default_storage as storage
		if not self.picture:
			return ""
		file_path = self.picture.name
		filename_base, filename_ext = os.path.splitext(file_path)
		thumbnail_file_path = "%s_thumbnail.jpg" % filename_base
		if storage.exists(thumbnail_file_path):
			#if thumbnail version exists, return its URL path
			return storage.url(thumbnail_file_path)
		# return original as a fallback
		return self.picture.url
