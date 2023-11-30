from django.urls import path

from SalesResults import views

urlpatterns = [
    # Urls De Sorteo
    path('sales/', views.SalesResultsAPIView.as_view()),
]