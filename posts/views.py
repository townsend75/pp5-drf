from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from django.http import HttpRequest, HttpResponse




class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        reviews_count=Count('reviews', distinct=True),
        average_rating= round (Avg('reviews__rating', 2
        ))
       
       
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
        'review_count'
        
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        # pk = self.kwargs.get('pk')
        # post = Post.objects.get(pk=pk)

        # review_user = Review.objects.get(review_user=review_user)
        # review_queryset = Review.objects.filter(post=post, review_user=review_user)

        # number_rating = self.objects.get(number_rating=number_rating)
        # avg_rating = self.objects.get(avg_rating=avg_rating).count()

        # # if review_queryset.exists():
        # #   raise ValidationError('You have already reviewed this post!')


        # # if number_rating == 0:
        # #     avg_rating = serializer.validated_data['rating']   
        
        # avg_rating = (avg_rating + serializer.validated_data['rating']/(number_rating))
           
             

        # number_rating = number_rating + 1   
        # post.save()  

        # serializer.save(post=post, review_user=review_user) 

       


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
       
        
    ).order_by('-created_at')