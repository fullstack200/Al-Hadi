from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .permissions import IsMosqueAdmin
# Create your views here.

from .models import Mosques, Prayers
from .serializers import MosqueSerializer, PrayerSerializer

class ListMosques(generics.ListAPIView):
    queryset = Mosques.objects.all()
    serializer_class = MosqueSerializer
    
class DetailMosque(generics.RetrieveAPIView):
    queryset = Mosques.objects.all()
    serializer_class = MosqueSerializer
    
    def get(self, request, *args, **kwargs):
        mosque = self.get_object()
        prayers = Prayers.objects.filter(mosque_id=mosque.mosque_id)  # Get all prayers for this mosque
        prayer_serializer = PrayerSerializer(prayers, many=True)  # Serialize the prayers

        # Combine the mosque data and the prayers data
        mosque_data = self.get_serializer(mosque).data
        mosque_data['prayers'] = prayer_serializer.data  # Add prayers to the mosque data
        
        return Response(mosque_data)

class AddMosqueView(generics.CreateAPIView):
    serializer_class = MosqueSerializer
    permission_classes = [IsMosqueAdmin]
    http_method_names = ['post']
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        return Response({"detail": "This method is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class ListNEditMosqueView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        mosque_id = self.kwargs['mosque_id']
        return Mosques.objects.filter(mosque_id=mosque_id)
    
    lookup_field = 'mosque_id'
    serializer_class = MosqueSerializer
    permission_classes = [IsMosqueAdmin]
    
class ListNAddPrayerView(generics.ListCreateAPIView):
    serializer_class = PrayerSerializer
    permission_classes = [IsMosqueAdmin]

    def get_queryset(self):
        mosque_id = self.kwargs['mosque_id']
        return Prayers.objects.filter(mosque_id=mosque_id)

    def post(self, request, mosque_id):
        # Create a mutable copy of request.data
        data = request.data.copy()
        print(data)
        data['mosque_id'] = mosque_id  # Set the mosque ID in the request data

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListNEditPrayerView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific prayer.
    """
    serializer_class = PrayerSerializer 
    lookup_field = 'prayer_id'
    permission_classes = [IsMosqueAdmin]

    def get_queryset(self):
        mosque_id = self.kwargs['mosque_id']
        return Prayers.objects.filter(mosque_id=mosque_id)