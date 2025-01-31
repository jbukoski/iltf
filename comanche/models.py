from django.contrib.gis.db import models
from django.contrib.gis import geos

# Counties model

class counties(models.Model):
    counties_id = models.AutoField(primary_key=True)
    objectid = models.IntegerField()
    name = models.CharField(max_length=32)
    state_name = models.CharField(max_length=35)
    state_fips = models.CharField(max_length=2)
    cnty_fips = models.CharField(max_length=3)
    fips = models.CharField(max_length=5)
    population = models.IntegerField()
    pop_sqmi = models.FloatField()
    pop2010 = models.IntegerField()
    pop10_sqmi = models.FloatField()
    white = models.IntegerField()
    black = models.IntegerField()
    ameri_es = models.IntegerField()
    asian = models.IntegerField()
    hawn_pi = models.IntegerField()
    hispanic = models.IntegerField()
    other = models.IntegerField()
    mult_race = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    age_under5 = models.IntegerField()
    age_5_9 = models.IntegerField()
    age_10_14 = models.IntegerField()
    age_15_19 = models.IntegerField()
    age_20_24 = models.IntegerField()
    age_25_34 = models.IntegerField()
    age_35_44 = models.IntegerField()
    age_45_54 = models.IntegerField()
    age_55_64 = models.IntegerField()
    age_65_74 = models.IntegerField()
    age_75_84 = models.IntegerField()
    age_85_up = models.IntegerField()
    med_age = models.FloatField()
    med_age_m = models.FloatField()
    med_age_f = models.FloatField()
    households = models.IntegerField()
    ave_hh_sz = models.FloatField()
    hsehld_1_m = models.IntegerField()
    hsehld_1_f = models.IntegerField()
    marhh_chd = models.IntegerField()
    marhh_no_c = models.IntegerField()
    mhh_child = models.IntegerField()
    fhh_child = models.IntegerField()
    families = models.IntegerField()
    ave_fam_sz = models.FloatField()
    hse_units = models.IntegerField()
    vacant = models.IntegerField()
    owner_occ = models.IntegerField()
    renter_occ = models.IntegerField()
    no_farms12 = models.FloatField()
    ave_size12 = models.FloatField()
    crop_acr12 = models.FloatField()
    ave_sale12 = models.FloatField()
    sqmi = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class boundaries(models.Model):
    boundary_id = models.AutoField(primary_key=True)
    aiannhce = models.CharField(max_length=4)
    aiannhns = models.CharField(max_length=8)
    affgeoid = models.CharField(max_length=13)
    geoid = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.boundary_id)


# Parcels models, in alphabetical order

class cotton(models.Model):
    cotton_id = models.AutoField(primary_key=True)
    parcelid = models.CharField(max_length=34)
    ag_acres = models.FloatField()
    asd_acres = models.FloatField()
    agparcelid = models.CharField(max_length=25)
    parcelid_1 = models.CharField(max_length=254)
    owner = models.CharField(max_length=254)
    addr1 = models.CharField(max_length=254)
    addr2 = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    st = models.CharField(max_length=254)
    zip = models.CharField(max_length=254)
    school = models.BigIntegerField()
    acres = models.FloatField()
    ownerperc = models.FloatField()
    mktland = models.BigIntegerField()
    assdland = models.BigIntegerField()
    mktimp = models.BigIntegerField()
    assdimp = models.BigIntegerField()
    mktother = models.BigIntegerField()
    assdother = models.BigIntegerField()
    exemption = models.BigIntegerField()
    dblexempt = models.BigIntegerField()
    image = models.CharField(max_length=254)
    legal = models.CharField(max_length=254)

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.parcelid)

class caddo(models.Model):
    caddo_id = models.AutoField(primary_key=True)
    objectid = models.IntegerField()
    objectid_1 = models.IntegerField()
    parcel_id = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    rec_num = models.CharField(max_length=10)
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class grady(models.Model):
    objectid = models.IntegerField()
    label = models.CharField(max_length=5)
    name = models.CharField(max_length=24)
    acres = models.CharField(max_length=24)
    parcel = models.CharField(max_length=24)
    mpin = models.CharField(max_length=21)
    problem = models.CharField(max_length=12)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class jefferson(models.Model):
    objectid = models.IntegerField()
    label = models.CharField(max_length=3)
    name = models.CharField(max_length=24)
    acres = models.CharField(max_length=24)
    parcel = models.CharField(max_length=24)
    mpin = models.CharField(max_length=21)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class kiowa(models.Model):
    objectid_1 = models.IntegerField()
    objectid = models.IntegerField()
    parcelnum = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    acreage = models.FloatField()
    parcelid = models.CharField(max_length=254)
    owner = models.CharField(max_length=254)
    addr1 = models.CharField(max_length=254)
    addr2 = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    st = models.CharField(max_length=254)
    zip = models.CharField(max_length=254)
    school = models.CharField(max_length=254)
    acres = models.FloatField()
    ownerperc = models.FloatField()
    mktland = models.IntegerField()
    assdland = models.IntegerField()
    mktimp = models.IntegerField()
    assdimp = models.IntegerField()
    mktother = models.IntegerField()
    assdother = models.IntegerField()
    exemption = models.IntegerField()
    dblexempt = models.IntegerField()
    image = models.CharField(max_length=254)
    legal = models.CharField(max_length=254)
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class stephens(models.Model):
    objectid = models.IntegerField()
    label = models.CharField(max_length=5)
    name = models.CharField(max_length=24)
    acres = models.CharField(max_length=24)
    parcel = models.CharField(max_length=24)
    mpin = models.CharField(max_length=21)
    account = models.CharField(max_length=9)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)

class tillman(models.Model):
    objectid_1 = models.IntegerField()
    objectid = models.IntegerField()
    label = models.CharField(max_length=5)
    owner = models.CharField(max_length=24)
    acres = models.CharField(max_length=24)
    parcel = models.CharField(max_length=24)
    mpin = models.CharField(max_length=21)
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()

    geom = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return '%s' % (self.objectid)
