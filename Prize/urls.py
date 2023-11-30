from django.urls import path

from Prize import views

urlpatterns = [
    path('prize/', views.PrizesAPIView.as_view()),
    path('prize/<int:pk>/', views.PrizeAPIView.as_view()),
]