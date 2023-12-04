from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user= serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
