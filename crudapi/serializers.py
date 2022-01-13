from rest_framework import serializers
from .models import SkateboardParks
# Serializers allow complex data such as querysets and 
# model instances to be converted to native Python datatypes 
# that can then be easily rendered into JSON, XML or other content types.
class SkateboardParksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkateboardParks
        fields = '__all__'
