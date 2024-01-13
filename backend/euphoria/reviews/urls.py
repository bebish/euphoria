from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    FragnanceReviewListCreateView,
    FragnanceReviewDetailView,
    FragnanceReviewViewSet,
    ReviewCommentViewSet,
    LikeViewSet,
    OrderViewSet,
    OrderItemViewSet,
    RatingViewSet
)



router = DefaultRouter()
router.register(r'reviews', FragnanceReviewViewSet)
router.register(r'comments', ReviewCommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reviews/', FragnanceReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', FragnanceReviewDetailView.as_view(), name='review-detail'),
    path('comments/', ReviewCommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
]