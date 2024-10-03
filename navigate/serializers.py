from rest_framework import serializers

from .models import Mosques, Prayers

class MosquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosques
        fields = ('mosque_name', 'mosque_address','mosque_google_map_url')

class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayers
        fields = '__all__'