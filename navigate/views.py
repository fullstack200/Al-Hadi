from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.

from .models import Mosques, Prayers
from .serializers import MosquesSerializer, PrayerSerializer

class ListMosques(generics.ListAPIView):
    queryset = Mosques.objects.all()
    serializer_class = MosquesSerializer
    
class DetailMosques(generics.RetrieveAPIView):
    queryset = Mosques.objects.all()
    serializer_class = MosquesSerializer
    
    def get(self, request, *args, **kwargs):
        mosque = self.get_object()
        prayers = Prayers.objects.filter(mosque_id=mosque.mosque_id)  # Get all prayers for this mosque
        prayer_serializer = PrayerSerializer(prayers, many=True)  # Serialize the prayers

        # Combine the mosque data and the prayers data
        mosque_data = self.get_serializer(mosque).data
        mosque_data['prayers'] = prayer_serializer.data  # Add prayers to the mosque data
        
        return Response(mosque_data)
