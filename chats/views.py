from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room

class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()

        return Response(request.data, status=status.HTTP_200_OK)