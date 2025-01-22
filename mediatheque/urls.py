from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('membre.urls')),
    path('bibliothecaire/', include('bibliothecaire.urls')),
    path('admin/', admin.site.urls),
]
