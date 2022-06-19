from os import stat
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


def listar_notas(request):
    try:
        notas = Nota.objects.all().order_by('updated')
        serializer = NotaSerializer(notas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


def ver_nota(request, pk):
    try:
        notas = Nota.objects.get(id=pk)
        serializer = NotaSerializer(notas, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


def crear_nota(request):
    try:
        data = request.data
        note = Nota.objects.create(
            body=data['body']
        )
        serializer = NotaSerializer(note, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


def actualizar_nota(request, pk):
    try:
        data = request.data
        note = Nota.objects.get(id=pk)
        serializer = NotaSerializer(instance=note, data=data)
        if serializer.isvalid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"ok": False}, status=status.HTTP_400_BAD_REQUEST)


def borrar_nota(request, pk):
    try:
        nota = Nota.objects.get(id=pk)
        nota.delete()
        return Response("Nota eliminada", status=status.HTTP_200_OK)
    except:
        return Response({"ok": False}, status=status.HTTP_200_OK)
