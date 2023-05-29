from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from garage_management.models import Garage
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .token import get_user_token
from .models import User


# Create your views here.

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == "POST":
        data = request.data
        username = data['username']
        # user = None
        user = User.objects.filter(username=username)
        if user:
            message = {'message': 'user does exist'}
            return Response(message)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        else:
            message = {'save': False}
            return Response(message)
    return Response({'message': "hey bro"})


# {
#     "username":"mike",
#     "email":"mike@gmail.com",
#     "password":"123",
#     "phone":"0686666622",
#     "type":"garage"
# }

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        user_id = User.objects.get(username=username)
        if user_id.type == "garage":
            try:
                garage = Garage.objects.values('id', 'name', 'description', 'latitude', 'longitude').get(user_id=user_id)
            except:
                garage = {}
            response = {
                'msg': 'success',
                'user_id': user_id.id,
                'username': user_id.username,
                'email': user_id.email,
                'phone': user_id.phone,
                'type': user_id.type,
                'garage': garage,
                'tokens': get_user_token(user),
            }

        else:
            response = {
                'msg': 'success',
                'user_id': user_id.id,
                'username': user_id.username,
                'email': user_id.email,
                'phone': user_id.phone,
                'type': user_id.type,
                'tokens': get_user_token(user),
            }

        return Response(response)
    else:
        response = {
            'msg': 'Invalid username or password',
        }

        return Response(response)

# {
#     "username": "mike",
#     "password": "123"
# }


# for farmer i will phone number as username and password
