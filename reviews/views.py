from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)

        serializer.save(post=post, review_user=review_user) 

    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ReviewDetailSerializer
        permission_classes= [IsOwnerOrReadOnly] 
        queryset= Review.objects.all()   

        