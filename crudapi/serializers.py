from rest_framework import serializers
from .models import SkateboardParks

class SkateboardParksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkateboardParks
        fields = '__all__'
