from django.urls import path

from AdwardsPublications import views

urlpatterns = [
    # Urls De Sorteo
    path('raffle/', views.RaffleAPIView.as_view()),
    path('bet/', views.BetAPIView.as_view()),
    #path('lottery/<int:pk>/', views.LotteryAPIView.as_view()),
]
