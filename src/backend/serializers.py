from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import USGeology

class USGeologySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = USGeology

        geo_field = "geom"

        fields = (
            'id','state', 'orig_label','unit_name'
        )

        """ fields = (
            'state', 'orig_label', 'sgmc_label', 'unit_link',
            'unit_name', 'age_min', 'age_max', 'major1',
            'major2', 'major3', 'minor1', 'minor2',
            'minor3', 'minor4', 'minor5', 'incidental',
            'indetermin', 'ref_id', 'reference', 'generalize',
            'digital_ur', 'ngmdb1', 'ngmdb2', 'ngmdb3',
            'shape_leng', 'shape_area', 'ruleid', 'geom',
        ) """