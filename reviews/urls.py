from django.urls import path
from reviews import views

urlpatterns = [
    path('<int:pk>/reviews', views.ReviewList.as_view(), name='reviews'),
    path('<int:pk>/review-create', views.ReviewCreate.as_view(), name='review_create'),
    # path('<int:pk>/review/', ReviewDetail.as_view(), name='review_detail')
]