from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.

class ProfileManager(BaseUserManager):

	def create_user(self, email, name, password=None):
		"""Create a User """
		if not email :
			raise ValueError('User must have an Email Address')

		email = self.normalize_email(email)
		user = self.model(email=email ,name=name)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):

		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user

class Profile(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=100, unique= True)
	name = models.CharField(max_length=100)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	objects = ProfileManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	
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
	image = models.ImageField(upload_to='Image')
	name = models.CharField(max_length=100, null=True)
	reference = models.CharField(max_length=100, null=True)
	category =  models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
	price = models.IntegerField()
	quantity = models.IntegerField()
	status = models.CharField(max_length=6, default='Active')

	def __str__(self):
		return self.name