from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sports/', include('Sports.urls')),
    path('lottery/', include('Lottery.urls')),
    path('1/', include('Prize.urls')),
<<<<<<< HEAD
    path('sports/', include ('Athletics.urls')),
    path('adwards_publications/', include('AdwardsPublications.urls')),
    path('adwards_publications_bet/', include('AdwardsPublicationsBet.urls')),
    path('sales_results/', include('SalesResults.urls')),
=======
    path('sports/', include('Athletics.urls')),
    path('raffle/', include('Raffle.urls'))
>>>>>>> 6df3c703e08ed5a4d573aa46cce11fa63b074135
]
