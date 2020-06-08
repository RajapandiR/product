from django.contrib import admin
from productapp import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Category)
admin.site.register(models.Product)