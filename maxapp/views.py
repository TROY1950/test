from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    django_logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

