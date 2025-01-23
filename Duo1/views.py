from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import requests


def home(request):
    return HttpResponse("Welcome to the homepage!")


def register_user(api_url, username, password):
    """
    Realiza una solicitud POST a la API de registro de usuario.

    :param api_url: str - URL de la API de registro
    :param username: str - Nombre de usuario
    :param email: str - Correo electrónico del usuario
    :param password: str - Contraseña del usuario
    :return: dict - Respuesta de la API (convertida a JSON) o error
    """
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP (4xx o 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}", "status_code": response.status_code}
    except requests.exceptions.RequestException as err:
        return {"error": f"Error occurred: {err}"}

# Ejemplo de uso
if __name__ == "__main__":
    api_url = "https://miapi.com/api/register/"  # Cambia esto por la URL de tu API
    username = "nuevo_usuario"
    password = "mi_contrase\u00f1a_segura"

    result = register_user(api_url, username, password)
    print(result)


@api_view(['GET','POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        print(username, password)
        User.objects.create_user(username=username, password=password)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def logout(request):
    django_logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


