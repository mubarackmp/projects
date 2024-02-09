# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Catogory(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	
class Products(models.Model):
	name = models.CharField(max_length=100)
	catogory = models.ForeignKey(Catogory, on_delete=models.CASCADE)
	description = models.TextField(null=True)
	stock = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='products/')

	def __str__(self):
		return self.name

class CartItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		
		return f'{self.quantity} x {self.product.name}'
