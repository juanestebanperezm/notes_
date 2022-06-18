from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@api_view(['GET'])
def get_routes(request):
    try:
        routes = []
        return Response(routes, status=status.HTTP_200_OK)
    except:
        return Response(":(", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_notes(request):
    try:
        notas = Nota.objects.all()
        serializer = NotaSerializer(notas, many=True)
        return Response(serializer.data)
    except:
        return Response(":(", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_note(request, pk):
    try:
        notas = Nota.objects.get(id=pk)
        serializer = NotaSerializer(notas, many=False)
        return Response(serializer.data)
    except:
        return Response(":(", status=status.HTTP_400_BAD_REQUEST)
