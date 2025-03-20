from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls', namespace='quotes')),  # Includes quotes app with namespace
]