from django.urls import path

from Lottery import views

urlpatterns = [
    # Urls De Sorteo
    path('lottery/', views.LotteryAPIView.as_view()),
    path('lottery/<int:pk>/', views.LotteryAPIView.as_view()),
]
