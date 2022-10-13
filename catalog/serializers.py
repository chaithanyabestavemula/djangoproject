from rest_framework import serializers
from .models import *

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
        