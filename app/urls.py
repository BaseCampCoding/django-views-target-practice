from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
]
