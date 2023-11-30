from django.urls import path

from AdwardsPublicationsBet import views

urlpatterns = [
    # Urls De Sorteo
    path('bet/', views.AdwardsPublicationsBetAPIView.as_view()),
]