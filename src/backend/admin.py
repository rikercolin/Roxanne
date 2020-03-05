from django.contrib.gis import admin
from .models import USGeology

admin.site.register(USGeology, admin.GeoModelAdmin)
