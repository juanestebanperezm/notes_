from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .utils import *


@api_view(['GET'])
def get_routes(request):
    try:
        routes = [
            
        ]
        return Response(routes, status=status.HTTP_200_OK)
    except:
        return Response(":(", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "POST"])
def get_notes(request):
    try:
        if request.method == "GET":
            return listar_notas(request)
        if request.method == "POST":
            return crear_nota(request)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_note(request, pk):
    try:
        if request.method == "GET":
            return ver_nota(request)
        if request.method == "PUT":
            return actualizar_nota(request, pk)
        if request.method == "DELETE":
            return borrar_nota(request, pk)

    except:
        return Response(":(", status=status.HTTP_400_BAD_REQUEST)


