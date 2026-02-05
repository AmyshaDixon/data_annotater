from django.contrib import admin
from django.urls import path, include

# Doesn't require leading slash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]