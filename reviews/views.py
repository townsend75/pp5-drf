from django.db.models import Count
from django.core.exceptions import ValidationError
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from posts.models import Post

class ReviewCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(post=post, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this post!')


        if post.number_rating == 0:
            post.avg_rating = serializer.validated_data['rating']   
        else:
             post.avg_rating = (post.avg_rating + serializer.validated_data['rating']/
             (post.number_rating))   

        post.number_rating = post.number_rating + 1   
        post.save()  

        serializer.save(post=post, review_user=review_user)    


class ReviewList(generics.ListAPIView):
        serializer_class = ReviewSerializer
        permission_classes= [permissions.IsAuthenticatedOrReadOnly] 
        queryset= Review.objects.all()   

        def get_queryset(self):
            pk = self.kwargs['pk']
            return Review.objects.filter(post=pk)