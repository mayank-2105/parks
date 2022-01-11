from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crudapi.models import SkateboardParks
from crudapi.serializers import SkateboardParksSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def parksApi(request,id=0):
    if request.method=='GET':
        parks = SkateboardParks.objects.all()
        parks_serializer=SkateboardParksSerializer(parks,many=True)
        return JsonResponse(parks_serializer.data,safe=False)
    elif request.method=='POST':
        parks_data=JSONParser().parse(request)
        parks_serializer=SkateboardParksSerializer(data=parks_data)
        if parks_serializer.is_valid():
            parks_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        parks_data=JSONParser().parse(request)
        parks=SkateboardParks.objects.get(ogc_fid=parks_data['ogc_fid'])
        parks_serializer=SkateboardParksSerializer(parks,data=parks_data)
        if parks_serializer.is_valid():
            parks_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        parks=SkateboardParks.objects.get(ogc_fid=id)
        parks.delete()
        return JsonResponse("Deleted Successfully",safe=False)