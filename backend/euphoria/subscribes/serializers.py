from http import HTTPStatus

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Subscribe
from users.serializers import UserSerializer
from users.models import User


class SubscribeSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода подписок пользователя."""

    class Meta:
        model = Subscribe
        fields = (
            "author",
            "user",
        )

    def validate(self, data):
        user = data.get("user")
        author = data.get("author")

        if Subscribe.objects.filter(user=user, author=author).exists():
            raise ValidationError(
                "Вы уже подписаны на этого автора"
            )
        if user == author:
            raise ValidationError(
                "Подписаться на самого себя невозможно",
                code=HTTPStatus.BAD_REQUEST,
            )
        return data

class SubscriptionSerializer(UserSerializer): #  НЕ ДОДЕЛАНО!!!!!!!!!
    """Сериалайзер для подписки."""

    review_count = serializers.ReadOnlyField(source="review.count")

    class Meta:
        model = User
        fields = (
            "username",
            "review_count",
        )