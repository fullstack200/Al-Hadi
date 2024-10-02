from django.urls import path
from .views import ListMosques, DetailMosques

urlpatterns = [ 
    path('', ListMosques.as_view()),
    path('<str:pk>/', DetailMosques.as_view()),
    
]