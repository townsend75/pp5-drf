
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import RatingSerializer, RatingDetailSerializer
from .models import Rating
from django.http import HttpRequest, HttpResponse
from posts.models import Post


def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
        post = Post.objects.get(id=post_id)
        Rating.objects.filter(post=post, user=request.user).delete()
        post.rating_set.create(user=request.user, rating=rating)
        return index(request) 

class RatingList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

       

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating
    update or delete a comment if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()

