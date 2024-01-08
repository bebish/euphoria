from rest_framework import serializers
from .models import FragnanceComment, Fragnance, Favourite, ShoppingList


class FragnanceSerializer(serializers.ModelSerializer):
    """Сериалайзер духов."""
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Fragnance
        fields = (
            'id',
            'title',
            'brand',
            'price',
            'image',
            'size',
            'available',
            'rating',
        )

    def get_rating(self, instance):
        comments = instance.comments.all()
        if comments.exists():
            total_rating = sum(comment.rating for comment in comments)
            return total_rating / comments.count()

class FragnanceCommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментариев к духам."""
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FragnanceComment
        fields = (
            'id',
            'rating',
            'text',
            'created_at'
        )

class FavouriteSerializer(serializers.ModelSerializer):
    """Сериалайзер для избранного."""

    class Meta:
        model = Favourite
        fields = (
            "user",
            "fragnance"
        )

    def validate(self, data):
        if self.Meta.model.objects.filter(
                user=data.get("user"), fragnance=data.get("fragnance")
        ).exists():
            raise serializers.ValidationError({
                "errors": 'Духи уже есть в избранном.'})
        return data

    def to_representation(self, instance):
        return FragnanceSerializer(
            instance.fragnance,
            context=self.context,
        ).data

class ShoppingListSerializer(FavouriteSerializer):
    """Сериализатор добавления духов в список покупок"""

    class Meta(FavouriteSerializer.Meta):
        model = ShoppingList
