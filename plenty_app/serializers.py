from .models import Plant
from rest_framework import serializers

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ("id", "name", "latin_name", "description", "illustration")