from rest_framework import serializers

from .models import Mosques, Prayers

class MosquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosques
        fields = ('mosque_name', 'mosque_address')

class PrayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prayers
        fields = ('prayer_name', 'prayer_rakat', 'azaan_time', 'prayer_time', 'prayer_valid_till' )