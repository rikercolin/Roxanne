from rest_framework import generics
from .models import USGeology
from .serializers import USGeologySerializer
from django.contrib.gis.geos import Point


class USGeologyListCreate(generics.ListAPIView):
    pnt_wkt = Point(-85.0, 45.0)

    queryset = USGeology.objects.filter(geom__contains=pnt_wkt)

    testset = USGeology.objects.filter(unit_name="Traverse Group")

    print(testset)
    print(queryset)
    serializer_class = USGeologySerializer
