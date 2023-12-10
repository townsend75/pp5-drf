from django.db import models
from django.contrib.auth.models import User
from posts.models import Post



class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField(max_length=200, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        


    def __str__(self):
        return f'{self.owner}, review'









