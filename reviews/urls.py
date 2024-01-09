from django.urls import path
from .views import FragnanceReviewListCreateView, FragnanceReviewDetailView

urlpatterns = [
    path('reviews/', FragnanceReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', FragnanceReviewDetailView.as_view(), name='review-detail'),
]