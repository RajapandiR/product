from rest_framework import serializers

from productapp import models

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Profile
		fields = ['id','firstName','lastName', 'userName','email', 'password','addressLine', 'city', 'zipcode', 'country', 'state']
		extra_kwargs = {
		'password': {
			'write_only': True,
			'style': {
				'input_type': 'password'
			}
		}
	}

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Category
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Product
		fields = '__all__'