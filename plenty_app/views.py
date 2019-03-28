from django.shortcuts import render
from .models import Plant
from .serializers import PlantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import ValidationError

class PlantList(APIView):
    def get(self, request, format=None):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True, context={"request":request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlantSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlantView(APIView):
    def get_object(self, pk):
        try:
            return Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        plant = self.get_object(pk=id)
        serializer = PlantSerializer(plant, context={"request":request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        plant = self.get_object(pk=id)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        plant = self.get_object(pk=id)
        serializer = PlantSerializer(plant,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)