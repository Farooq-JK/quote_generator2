from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.existing_quotes, name='existing_quotes'),
    path('create/', views.create_quote, name='create_quote'),
    path('download/<int:pk>/', views.download_quote, name='download_quote'),
    path('delete_all_quotes/', views.delete_all_quotes, name='delete_all_quotes'),
    path('delete/<int:pk>/', views.delete_quote, name='delete_quote'),  # Route for deleting a quote
]

