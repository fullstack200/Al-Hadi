from django.urls import path, include
from .views import ListMosques, DetailMosque, MosquePrayerDetailView, PrayerDetailView

urlpatterns = [ 
    path('', ListMosques.as_view()),
    path('<str:pk>/', DetailMosque.as_view()),
    path('<str:mosque_id>/addprayer/', MosquePrayerDetailView.as_view(), name='mosque-prayers'),
    path('<str:mosque_id>/editprayer/<str:prayer_id>/', PrayerDetailView.as_view(), name='prayer-detail'),   
    path('api-auth/', include('rest_framework.urls')),
]