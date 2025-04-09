from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


# Create your views here.
class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
