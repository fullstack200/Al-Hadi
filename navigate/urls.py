from django.urls import path, include
from .views import ListMosques, DetailMosque, ListNEditMosqueView, ListNAddPrayerView, ListNEditPrayerView

urlpatterns = [ 
    path('listmosque/', ListMosques.as_view(), name='List_Mosques'),
    path('detailmosque/<str:pk>/', DetailMosque.as_view(), name='List_Mosques_Details'),
    path('editmosque/<str:mosque_id>/',ListNEditMosqueView.as_view(), name='List_N_Edit_Mosques'),
    path('addprayer/<str:mosque_id>/', ListNAddPrayerView.as_view(), name='List_N_Add_Prayers'),
    path('editprayer/<str:mosque_id>/<str:prayer_id>/', ListNEditPrayerView.as_view(), name='List_N_Edit_Prayers'), 
]