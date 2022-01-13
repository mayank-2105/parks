from django.db import models
from django.contrib.gis.db import models as gismodels
# Create your models here.
#Here we have created the models for our countries shapefile
#Run 'python manage.py inspectdb' create the models after connecting your legacy database to django

class SkateboardParks(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    park_id = models.IntegerField(blank=True, null=True)
    facilityid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_fr = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    address_fr = models.CharField(max_length=80, blank=True, null=True)
    facility_t = models.CharField(max_length=80, blank=True, null=True)
    facility_1 = models.CharField(max_length=80, blank=True, null=True)
    accessctrl = models.CharField(max_length=80, blank=True, null=True)
    accessible = models.CharField(max_length=80, blank=True, null=True)
    open = models.CharField(max_length=80, blank=True, null=True)
    notes = models.CharField(max_length=80, blank=True, null=True)
    modified_d = models.DateField(blank=True, null=True)
    created_da = models.DateField(blank=True, null=True)
    facility = models.CharField(max_length=80, blank=True, null=True)
    facility_f = models.CharField(max_length=80, blank=True, null=True)
    descriptio = models.CharField(max_length=80, blank=True, null=True)
    descript_1 = models.CharField(max_length=80, blank=True, null=True)
    picture_li = models.CharField(max_length=80, blank=True, null=True)
    picture_de = models.CharField(max_length=80, blank=True, null=True)
    picture_1 = models.CharField(db_column='picture__1', max_length=80, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    longitude = models.DecimalField(blank=True, null=True,max_digits=19, decimal_places=13)
    latitude = models.DecimalField(blank=True, null=True,max_digits=19, decimal_places=13)
    max_strength= models.IntegerField(blank=True, null=True)
    no_of_gates= models.IntegerField(blank=True, null=True)
    # wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wkb_geometry= gismodels.PointField(srid=4326, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'skateboard_parkdata'

