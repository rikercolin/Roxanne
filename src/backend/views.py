from rest_framework import generics
from .models import USGeology
from .serializers import USGeologySerializer
from django.contrib.gis.geos import Point


class USGeologyListCreate(generics.ListCreateAPIView):
    pnt_wkt = Point(853600.00, 444500.00)

    queryset = USGeology.objects.filter(geom__contains=pnt_wkt)

    testset = USGeology.objects.filter(geom__intersects=pnt_wkt)

    print(testset)
    print(queryset)
    serializer_class = USGeologySerializer
