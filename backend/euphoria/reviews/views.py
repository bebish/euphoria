from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    FragnanceReview, ReviewComment, Like, Order, OrderItem, Rating
)
from .serializers import (
    FragnanceReviewSerializer,
    ReviewCommentSerializer,
    LikeSerializer,
    OrderSerializer,
    OrderItemSerializer,
    RatingSerializer
)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FragnanceReviewViewSet(ModelViewSet):
    """Вьюсет обзора духов."""
    queryset = FragnanceReview.objects.all()
    serializer_class = FragnanceReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['fragnance', 'text', 'rating']
    search_fields = ['title', 'description']

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class FragnanceReviewListCreateView(generics.ListCreateAPIView):
    queryset = FragnanceReview.objects.all()
    serializer_class = FragnanceReviewSerializer
    permission_classes = [IsAuthenticated]


class FragnanceReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FragnanceReview.objects.all()
    serializer_class = FragnanceReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewCommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев к обзору духов."""
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

