from django.db import models
from django.contrib.auth.models import User


# Create your models here.


"""
model for product category
"""
class Category(models.Model):
	CAT_MALE = 'male'
	CAT_FEMALE = 'female'
	CAT_CHILD = 'children'

	CATEGORY_CHOICES =(
		(CAT_MALE,'Male'),
		(CAT_FEMALE,'Female'),
		(CAT_CHILD,'Children'),
		)
	cat_name = models.CharField(max_length=100,choices=CATEGORY_CHOICES, null=True, blank=True)
	
	def __str__(self):		
		return self.cat_name

"""
model for the product size
"""
class Size(models.Model):
	LONG = 'long'
	MEDIUM = 'medium'
	SHORT = 'short'
	XL='xl'
	XXL='xxl'

	SIZE_CHOICES =(
		(LONG,'Long'),
		(MEDIUM,'Medium'),
		(SHORT,'Short'),
		(XL,'xl'),
		(XXL,'xxl')
		)
	size = models.CharField(max_length=50,choices=SIZE_CHOICES, null=True, blank=True)
	
	def __str__(self):		
		return self.size


"""
model for the product size
"""
class ProType(models.Model):
	SUMMER = 'summer'
	WINTER = 'winter'

	TYPE_CHOICES =(
		(SUMMER,'Summer'),
		(WINTER,'Winter'),
		)
	protype = models.CharField(max_length=50,choices=TYPE_CHOICES, null=True, blank=True)
	
	def __str__(self):		
		return self.protype


"""
product 
"""
class Product(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
	size = models.ManyToManyField(Size, help_text="select size of the product")
	product_type = models.ManyToManyField(ProType, help_text="select a product type")
	price = models.CharField(max_length=100, help_text="entet price of product")
	image = models.ImageField(upload_to='uploads/', null=True)
	
	def __str__(self):
		return self.product_title

	def get_absolute_url(self):
		return reverse('trooproduct:pro-detail', args=[str(self.id)])


"""
Mycart
"""
class mycart(models.Model):
	class Meta:
		ordering = ['item']		
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	item = models.CharField(max_length=200)
	
	def __str__():
		return '{} {}'.format(self.user, self.item)

