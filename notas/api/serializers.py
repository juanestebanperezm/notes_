from ast import Mod
from dataclasses import fields
from .models import *
from rest_framework.serializers import ModelSerializer


class NotaSerializer(ModelSerializer):
    class Meta:
        model = Nota 
        fields = '__all__'