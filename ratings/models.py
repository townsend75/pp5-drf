from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class RatingChoices(models.IntegerChoices):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    


class Rating(models.Model):
    """
    Rating model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    value = models.IntegerField(choices=RatingChoices.choices)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content