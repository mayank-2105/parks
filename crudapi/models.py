from django.db import models

# Create your models here.
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
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'skateboard_parks'

