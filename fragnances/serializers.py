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
            'type',
            'sex',
            'image',
            'size',
            'available',
            'rating',
            'description'
        )

    def get_rating(self, instance):
        comments = instance.comments.all()
        if comments.exists():
            total_rating = sum(comment.rating for comment in comments)
            return total_rating / comments.count()
        return 'Оценок пока нет'

    def validate_image(self, image):
        supported_formats = ["jpg", "jpeg", "png"]
        file_extension = image.name.split('.')[-1]
        if not image:
            raise serializers.ValidationError(
                {'image': "Нужна картинка."}
            )
        if file_extension.lower() not in supported_formats:
            raise serializers.ValidationError(
                {'file_extension': "Непонятный формат картинки."}
            )
        return image

class FragnanceCommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для комментариев к духам."""

    class Meta:
        model = FragnanceComment
        fields = (
            'id',
            'rating',
            'text',
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

class ShoppingListSerializer(FavouriteSerializer): #  НЕ ДОДЕЛАНО
    """Сериализатор добавления духов в список покупок"""

    class Meta(FavouriteSerializer.Meta):
        model = ShoppingList

    def validate(self, data):
        if self.Meta.model.objects.filter(
                user=data.get("user"), fragnance=data.get("fragnance")
        ).exists():
            raise serializers.ValidationError({
                "errors": 'Духи уже есть в списке.'})
        return data



