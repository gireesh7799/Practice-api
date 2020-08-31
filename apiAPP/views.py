from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class ApiView(APIView):

    serializer_class = apiapp_serializers
    
    def get(self, request):
        
        customer_list = Fields.objects.all()
        serializer = self.serializer_class(customer_list, many=True)
        return Response(serializer.data)


    def post(self, request):
        
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(): 
            if serialize.validated_data.get('end_date') >= serialize.validated_data.get('start_date'):
                uses = serialize.save()
                uses.code = '1000'+str(uses.id)
                uses.revenue = uses.cpi*uses.completes
                uses.save()
                return Response(serialize.data, status=201)
            else:
                return Response({'error':'end_date must be greater than start_date'}, status=404)
        return Response(serialize.errors, status=400)


class ApiUpdateView(APIView):


    serializer_class = apiapp_serializers

    def get_object(self, id):
        
        try:
            return Fields.objects.get(id=id)
        except Fields.DoesNotExist as e:
            return None

    def get(self, request, id=None):
        
        instance = self.get_object(id)
        if instance != None:
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        else:
            return Response({'errors': 'given customer organization object not found'}, status=404)

    def put(self, request, id):
        
        instance = self.get_object(id)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)