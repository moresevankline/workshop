from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserDataSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class UserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
