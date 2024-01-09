from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FragnanceReview
from .serializers import FragnanceReviewSerializer

class FragnanceReviewListCreateView(generics.ListCreateAPIView):
    queryset = FragnanceReview.objects.all()
    serializer_class = FragnanceReviewSerializer
    permission_classes = [IsAuthenticated]

class FragnanceReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FragnanceReview.objects.all()
    serializer_class = FragnanceReviewSerializer
    permission_classes = [IsAuthenticated]
# Create your views here.
