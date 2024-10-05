from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mosques, Prayers


class MosqueSerializer(serializers.ModelSerializer):
    mosqueAdmin = serializers.CharField(source='mosqueAdmin.username', read_only=True)
    class Meta:
        model = Mosques
        fields = '__all__'
        
    def create(self, validated_data):
        # Get the authenticated user from the request context
        user = self.context['request'].user
        # Set the mosqueAdmin to the authenticated user
        mosque = Mosques.objects.create(mosqueAdmin=user, **validated_data)
        return mosque

class PrayerSerializer(serializers.ModelSerializer):
    mosque_id = serializers.PrimaryKeyRelatedField(
        queryset=Mosques.objects.all(), 
        label='Mosque Name'  # Change the label here
    )
    mosqueAdmin = serializers.CharField(source='mosqueAdmin.username', read_only=True)  # Get username from mosqueAdmin

    class Meta:
        model = Prayers
        fields = '__all__'
        
    def create(self, validated_data):
        # Get the authenticated user from the request context
        user = self.context['request'].user
        # Set the mosqueAdmin to the authenticated user
        prayer = Prayers.objects.create(mosqueAdmin=user, **validated_data)
        return prayer