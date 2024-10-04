from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mosques(models.Model):
    mosque_id = models.CharField(max_length=50,primary_key=True)
    mosque_name = models.CharField(max_length=100)
    mosque_address = models.CharField(max_length=500)
    mosque_google_map_url = models.URLField(max_length=500)
    mosqueAdmin = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # Add 'Masjid E' prefix if not already present
        if not self.mosque_name.startswith('Masjid E'):
            self.mosque_name = f"Masjid E {self.mosque_name}"
        super(Mosques, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.mosque_name
    
class Prayers(models.Model):
    prayer_id = models.CharField(max_length=50, primary_key=True)
    prayer_name = models.CharField(max_length=100)
    prayer_rakat = models.IntegerField()
    azaan_time = models.TimeField(blank=True, null=True)
    prayer_time = models.TimeField(blank=True, null=True)
    prayer_valid_till = models.TimeField(blank=True, null=True)
    mosque_id = models.ForeignKey(Mosques, related_name='prayers', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.prayer_name

    


