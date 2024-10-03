from django.urls import path
from .views import ListMosques, DetailMosques, MosquePrayerDetailView, PrayerDetailView

urlpatterns = [ 
    path('', ListMosques.as_view()),
    path('<str:pk>/', DetailMosques.as_view()),
    path('<str:mosque_id>/addprayers/', MosquePrayerDetailView.as_view(), name='mosque-prayers'),
    path('<str:mosque_id>/editprayer/<str:prayer_id>/', PrayerDetailView.as_view(), name='prayer-detail'),   
]