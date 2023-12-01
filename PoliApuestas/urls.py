from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sports/', include('Sports.urls')),
    path('1/', include('Prize.urls')),
    path('sports/', include('Athletics.urls')),
    path('raffle/', include('Raffle.urls'))
]
