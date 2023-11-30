from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sports/', include('Sports.urls')),
    path('lottery/', include('Lottery.urls')),
    path('1/', include('Prize.urls')),
    path('sports/', include ('Athletics.urls')),
    path('adwards_publications/', include('AdwardsPublications.urls')),
    path('adwards_publications_bet/', include('AdwardsPublicationsBet.urls')),
    path('sales_results/', include('SalesResults.urls')),
]
