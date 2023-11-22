from django.urls import path

from Sports import views

urlpatterns = [
    path('championship/', views.ChampionshipsAPIView.as_view()),
    path('championship/<int:pk>/', views.ChampionshipAPIView.as_view()),
]