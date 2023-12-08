from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/<int:pk>', views.ReviewList.as_view(), name='reviews'),
    path('review-create/<int:pk>', views.ReviewCreate.as_view(), name='review_create'),
    # path('<int:pk>/review/', ReviewDetail.as_view(), name='review_detail')
]