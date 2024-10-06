from django.contrib import admin
from .models import Mosques, Prayers

class PrayerAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('prayer_id', 'prayer_name', 'prayer_rakat', 'azaan_time', 'prayer_time', 'get_mosque_name')

    def get_mosque_name(self, obj):
        # Return the name of the mosque instead of the mosque ID
        return obj.mosque_id.mosque_name  # Assuming 'mosque_id' is the related name

    get_mosque_name.short_description = 'Mosque Name'  # Set the label for this column

    def get_form(self, request, obj=None, **kwargs):
        # Get the form
        form = super().get_form(request, obj, **kwargs)
        
        # Change the label for the mosque_id field in the form
        form.base_fields['mosque_id'].label = "Mosque Name"
        
        return form
    
class MosqueAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('mosque_id', 'mosque_name', 'mosque_address', 'mosque_google_map_url', 'mosqueAdmin')

    def get_form(self, request, obj=None, **kwargs):
        # Get the form
        form = super().get_form(request, obj, **kwargs)
        
        # Change the label for the mosque_id field (if applicable)
        form.base_fields['mosque_id'].label = "Mosque Name"  # Change this to the relevant field

        return form

admin.site.register(Mosques, MosqueAdmin)
admin.site.register(Prayers, PrayerAdmin)

