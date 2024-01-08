from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания и получение списка пользователей."""

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
        )
