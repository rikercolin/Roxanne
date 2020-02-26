from django.contrib.gis.db import models


class USGeology(models.Model):
    state = models.CharField(max_length=2)
    orig_label = models.CharField(max_length=12)
    sgmc_label = models.CharField(max_length=16)
    unit_link = models.CharField(max_length=18)
    unit_name = models.CharField(max_length=254)
    age_min = models.CharField(max_length=100, null=True)
    age_max = models.CharField(max_length=100, null=True)
    major1 = models.CharField(max_length=30, null=True)
    major2 = models.CharField(max_length=30, null=True)
    major3 = models.CharField(max_length=30, null=True)
    minor1 = models.CharField(max_length=30, null=True)
    minor2 = models.CharField(max_length=30, null=True)
    minor3 = models.CharField(max_length=30, null=True)
    minor4 = models.CharField(max_length=30, null=True)
    minor5 = models.CharField(max_length=100, null=True)
    incidental = models.CharField(max_length=175, null=True)
    indetermin = models.CharField(max_length=150, null=True)
    ref_id = models.CharField(max_length=6)
    reference = models.CharField(max_length=254)
    generalize = models.CharField(max_length=100)
    digital_ur = models.CharField(max_length=125, null=True)
    ngmdb1 = models.CharField(max_length=100, null=True)
    ngmdb2 = models.CharField(max_length=100, null=True)
    ngmdb3 = models.CharField(max_length=100, null=True)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    ruleid = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.unit_name

