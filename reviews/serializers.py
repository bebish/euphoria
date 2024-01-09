from rest_framework import serializers
from .models import FragnanceReview

class FragnanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FragnanceReview
        fields = '__all__'