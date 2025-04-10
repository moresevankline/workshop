from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "country",
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            country=validated_data["country"],
        )
        return user


class UserDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "country")
