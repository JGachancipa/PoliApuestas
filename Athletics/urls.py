from django.urls import path

from Athletics import views

urlpatterns = [
    # Urls De deportes
    path('athletics/', views.AthleticssAPIView.as_view()),
    path('athletics/<int:pk>/', views.AthleticsAPIView.as_view()),
]