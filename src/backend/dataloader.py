import os
from django.contrib.gis.utils import LayerMapping
from .models import USGeology

usgeology_mapping = {
    'state': 'STATE',
    'orig_label': 'ORIG_LABEL',
    'sgmc_label': 'SGMC_LABEL',
    'unit_link': 'UNIT_LINK',
    'unit_name': 'UNIT_NAME',
    'age_min': 'AGE_MIN',
    'age_max': 'AGE_MAX',
    'major1': 'MAJOR1',
    'major2': 'MAJOR2',
    'major3': 'MAJOR3',
    'minor1': 'MINOR1',
    'minor2': 'MINOR2',
    'minor3': 'MINOR3',
    'minor4': 'MINOR4',
    'minor5': 'MINOR5',
    'incidental': 'INCIDENTAL',
    'indetermin': 'INDETERMIN',
    'ref_id': 'REF_ID',
    'reference': 'REFERENCE',
    'generalize': 'GENERALIZE',
    'digital_ur': 'DIGITAL_UR',
    'ngmdb1': 'NGMDB1',
    'ngmdb2': 'NGMDB2',
    'ngmdb3': 'NGMDB3',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'ruleid': 'RuleID',
    'geom': 'MULTIPOLYGON',
}


usgeology_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..','..','GISData','Converted_Geology', 'Geology_LatLon.shp'),
)

def run(verbose=True):
    lm = LayerMapping(USGeology, usgeology_shp, usgeology_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)