from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework import generics
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    description = models.CharField(max_length=200, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        


    def __str__(self):
        return f'{self.rating} {self.post.title}'









