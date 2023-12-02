from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.db.models import Avg


RATING_CHOICES = [
        (0, '0'),
        (1, '1'), 
        (2, '2 '),
        (3, '3 '),
        (4, '4 '),
        (5, '5')
    ]
    


class Rating(models.Model):
    """
    Rating model, related to User and Post
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    value = models.PositiveIntegerField(
        choices=RATING_CHOICES, default=0)
       

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return self.content