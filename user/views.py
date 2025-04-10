from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["POST"])
def user_register_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
