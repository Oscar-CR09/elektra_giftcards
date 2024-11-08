from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarjeta
from .serializers import TarjetaSerializer

class TarjetaView(APIView):
    def post(self, request):
        # Crear una nueva tarjeta
        serializer = TarjetaSerializer(data=request.data)
        if serializer.is_valid():
            tarjeta = serializer.save()
            return Response(TarjetaSerializer(tarjeta).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        # Consultar tarjeta por ID
        try:
            tarjeta = Tarjeta.objects.get(id=id)
            return Response(TarjetaSerializer(tarjeta).data)
        except Tarjeta.DoesNotExist:
            return Response({"error": "Tarjeta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
