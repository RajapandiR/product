from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

from productapp import models as m
# Create your models here.

class ProfileManager(BaseUserManager):

	def create_user(self, email, userName, password=None):
		"""Create a User """
		if not email :
			raise ValueError('User must have an Email Address')

		email = self.normalize_email(email)
		user = self.model(email=email ,userName=userName)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, userName, password):

		user = self.create_user(email, userName, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class Profile(AbstractBaseUser, PermissionsMixin):
	userName = models.CharField(max_length=100, null=True, unique= True)
	email = models.EmailField(max_length=100, unique= True)
	firstName = models.CharField(max_length=100, null=True)
	lastName = models.CharField(max_length=100, null=True)
	addressLine = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	zipcode = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)
	state = models.CharField(max_length=100, null=True)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	objects = ProfileManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['userName']
	
	def get_full_name(self):
		return self.name

	def __str__(self):
		return self.email

class Category(models.Model):
	name = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=200, null=True)
	displayed = models.CharField(max_length=5,default='Yes')
	created_on = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	TAXRULE = (
		('No tax', 'No tax'), 
		('Tax (9%)', 'Tax (9%)'),
		('Tax (12%)', 'Tax (12%)'),
		('Tax (15%)', 'Tax (15%)'),
		('Tax (18%)', 'Tax (18%)'),
	)
	image = models.ImageField(upload_to='Image')
	name = models.CharField(max_length=100, null=True)
	reference = models.CharField(max_length=100, null=True)
	category =  models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
	price = models.IntegerField(null=True)
	taxexcl =  models.IntegerField(null=True)
	taxincl = models.IntegerField(null=True)
	taxrule = models.CharField(max_length=100, choices= TAXRULE,null=True)
	quantity = models.IntegerField(null=True)
	status = models.CharField(max_length=6, default='Active')
	created_on = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	total = models.IntegerField(null=True)
	created_on = models.DateTimeField(auto_now_add=True, null=True)

class Invoice(models.Model):
	def increment_invoice_number():
		last_invoice = Invoice.objects.all().order_by('id').last()
		if not last_invoice:
		     return 'XXX0001'
		invoiceNo = last_invoice.invoiceNo
		invoice_int = int(invoiceNo.split('XXX')[-1])
		width = 4
		new_invoice_int = invoice_int + 1
		formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
		new_invoice_no = 'XXX' + str(formatted)
		return new_invoice_no
	enableInvoice = models.CharField(max_length=100,default = 'Yes',) 
	invoicePrefix = models.CharField(max_length=100, null=True) 
	invoiceNo = models.CharField(max_length=500, default=increment_invoice_number, null=True, blank=True)
	footerText = models.CharField(max_length=100, null=True) 

	def __str__(self):
		return self.invoiceNo