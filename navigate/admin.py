from django.contrib import admin
from .models import MosqueAdmin, Mosques, Prayers
# Register your models here.

admin.site.register(MosqueAdmin)
admin.site.register(Mosques)
admin.site.register(Prayers)

