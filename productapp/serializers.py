from rest_framework import serializers

from productapp import models

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Profile
		fields = ['email', 'name', 'password']
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