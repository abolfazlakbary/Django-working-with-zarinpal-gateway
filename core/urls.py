from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('market/', include('market.urls')),
    path('api/v1/', include('api.urls')),
    path('buy/', include('zarinpal.urls')),
]
