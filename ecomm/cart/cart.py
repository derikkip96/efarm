from django.conf import settings
from decimal import Decimal
from efarm.models import Product
from coupons.models import Coupon

class Cart(object):
	# initialise cart session

	def __init__(self,request):
		# gettin the current session
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			#save empty cart
			cart =self.session[settings.CART_SESSION_ID]={}
		self.cart = cart
		# store the current coupon
		self.coupon_id = self.session.get('coupon_id')
	def remove(self,product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def add(self,product, quantity=1,update_quantity=False):
		# add a product to the shopping cart or update its quantity
		product_id =str(product.id)
		# checking if the product is not in the cart
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0,
									'price':str(product.price)}

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity

		else:
			self.cart[product_id]['quantity'] +=quantity

		self.save()
	
	def save(self):
		# update the session cart
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modified = True

	def __iter__(self):
		# iterate over the items in the cart and get products from the datebase
		products_id= self.cart.keys()

		# retrieving product instances availabe in the cart and add the to the item cart
		products = Product.objects.filter(id__in =products_id)
		for product in products:
			self.cart[str(product.id)]['product'] = product
  
		# iterating over the items in the shopping cart and getting the total price
		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] =item['price']*item['quantity']
			yield item
	def __len__(self):
		# summing up the total items in the shopping cart
		return sum(item['quantity' ] for item in self.cart.values())
	
	def get_the_total_cost(self):
		return sum(item['quantity']*Decimal(item['price']) for item in self.cart.values())

	@property
	def coupon(self):
		if self.coupon_id:
			return Coupon.objects.get(id=self.coupon_id)
		return None
	def get_discount(self):
		if self. coupon:
			return(self.coupon.discount/Decimal('100')\
			 * self.get_the_total_cost())
		return Decimal('0')
	def get_total_cost_after_discount(self):
		return self.get_the_total_cost() - self.get_discount()

	def clear(self):
		# remove cart from the session
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True