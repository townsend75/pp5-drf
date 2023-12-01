from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id', 'content', 'owner', 'post', 'value',
            'created_at',
        ]

class RatingDetailSerializer(RatingSerializer):
    post = serializers.ReadOnlyField(source='post.id')         