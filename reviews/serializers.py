from rest_framework import serializers
from .models import FragnanceReview, ReviewComment, Like, Order, OrderItem, Rating

class FragnanceReviewSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField()
    image = serializers.ImageField()
    class Meta:
        model = FragnanceReview
        fields = ['id', 'title', 'video_url', 'image', 'user', 'text', 'created_at']

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'