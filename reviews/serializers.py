from rest_framework import serializers;
from reviews.models import Review;
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReviewSerializer(serializers.ModelSerializer):

    """ Serializer for the review model"""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            "id",
            "owner",
            "is_owner",
            'post',
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "content",
            "rating",
        ]

class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source="post.id")        
