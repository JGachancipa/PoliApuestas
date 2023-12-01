from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from Raffle import views

router = routers.DefaultRouter()
router.register(r'Raffle', views.RaffleView, 'Raffle')

# Crear las rutas (GET, POST, PUT, DELETE)
urlpatterns = [
    # Indica como va a ser citada la URL, se agrega las versiones para las API-VERSIONS.
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Raffle API"))
]