from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin



@api_view(['GET'])
def deb(request):
    cat=product.objects.all()
    serializer=productserializer(cat,many=True)
    return Response(serializer.data)

#POSTING DATA
@api_view(['POST'])
def debu(request):
    cat=product.objects.all()
    serializer=productserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
class student(GenericAPIView,ListModelMixin):
    queryset = product.objects.all()
    serializer_class = productserializer
    def get(self,request):
        return self.list(request)
class studentcreate(GenericAPIView,CreateModelMixin):
    queryset = product.objects.all()
    serializer_class = productserializer
    def post(self,request):
        return self.create(request)



# Create your views here.
