from django.urls import path
from ratings import views

urlpatterns = [
    # path('rate/', views.RatingList.as_view()),
    path('rate', views.rate),
    path('rate/<int:pk>/', views.RatingList.as_view()),
]