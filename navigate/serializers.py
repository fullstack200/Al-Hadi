from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mosques, Prayers


class MosqueSerializer(serializers.ModelSerializer):
    mosqueAdmin = serializers.CharField(source='mosqueAdmin.username', read_only=True)
    class Meta:
        model = Mosques
        fields = '__all__'

class PrayerSerializer(serializers.ModelSerializer):
    mosqueAdmin = serializers.CharField(source='mosqueAdmin.username', read_only=True)  # Getting username from mosqueAdmin
    
    class Meta:
        model = Prayers
        fields = '__all__'