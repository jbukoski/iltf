import os
from django.contrib.gis.utils import LayerMapping
from . import models

# Admin mappings and shapefiles

boundary_mapping = {
    'id' : 'Id',
    'area' : 'Area',
    'perimeter' : 'Perimeter',
    'acres' : 'Acres',
    'comments' : 'Comments',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'boundary.shp'))

buffered_bndry_mapping = {
    'dn' : 'DN',
    'geom' : 'MULTIPOLYGON',
}

buffered_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'boundary_buffered.shp'))

ag_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'acres' : 'ACRES',
    'use' : 'USE',
    'service' : 'SERVICE',
    'ag_id' : 'ID',
    'status' : 'STATUS',
    'group' : 'GROUP',
    'owner' : 'Owner',
    'dissolve' : 'dissolve',
    'tract_numb' : 'Tract_Numb',
    'ownership' : 'Ownership',
    'community' : 'Community',
    'soc_count' : 'soc_count',
    'soc_sum' : 'soc_sum',
    'soc_mean' : 'soc_mean',
    'soctotal' : 'socTotal',
    'socmean' : 'socMean',
    'geom' : 'MULTIPOLYGON',
}

ag_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'agriculture', 'ag_lands.shp'))

vineyards_mapping = {
    'vineyard_id' : 'Id',
    'acres' : 'Acres',
    'section' : 'Section',
    'soc_count' : 'soc_count',
    'soc_sum' : 'soc_sum',
    'soc_mean' : 'soc_mean',
    'soc_min' : 'soc_min',
    'soc_max' : 'soc_max',
    'soctotal' : 'socTotal',
    'socmean' : 'socMean',
    'geom' : 'MULTIPOLYGON',
}

vineyards_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'vineyards', 'vineyards.shp'))

mbls_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'mbl_field' : 'MBL_',
    'mbl_id' : 'MBL_ID',
    'acres' : 'ACRES',
    'entity' : 'Entity',
    'outboundsp' : 'OUTBOUNDSP',
    'outbound_1' : 'OUTBOUND_1',
    'comment' : 'COMMENT',
    'boundary_m' : 'BOUNDARY_M',
    'boundary_1' : 'BOUNDARY_1',
    'lotid' : 'LotID',
    'santa_ana' : 'Santa_Ana',
    'owner' : 'Owner',
    'acres_txt' : 'Acres_txt',
    'dissolve' : 'dissolve',
    'entity2' : 'Entity2',
    'soc_count' : 'soc_count',
    'soc_sum' : 'soc_sum',
    'soc_mean' : 'soc_mean',
    'soc_min' : 'soc_min',
    'soc_max' : 'soc_max',
    'soctotal' : 'socTotal',
    'socmean' : 'socMean',
    'geom' : 'POLYGON',
}

mbls_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'mbl_int', 'mbl_int.shp'))

roads_mapping = {
    'length' : 'LENGTH',
    'id_field' : 'ID__',
    'access' : 'ACCESS',
    'name' : 'NAME',
    'number' : 'NUMBER',
    'surface' : 'SURFACE',
    'condition' : 'CONDITION',
    'road_class' : 'CLASS',
    'road_type' : 'TYPE',
    'sa_id' : 'SA_ID',
    'surf_type' : 'Surf_Type',
    'status' : 'Status',
    'hunting' : 'Hunting',
    'comment' : 'Comment',
    'restrict' : 'Restrict',
    'roadrepair' : 'RoadRepair',
    'geom' : 'MULTILINESTRING',
}

roads_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'reservation_roads.shp'))

# HYDROLOGY LAYERS

watersheds_mapping = {
    'objectid' : 'OBJECTID',
    'source' : 'Source',
    'huc_8' : 'HUC_8',
    'hu_8_name' : 'HU_8_Name',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

watersheds_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'psa_watershedbasins_4326.shp'))

subwatersheds_mapping = {
    'id' : 'Id',
    'watershed' : 'Watershed',
    'subwatshed' : 'SubWatshed',
    'wsno' : 'wsNo',
    'acres' : 'Acres',
    'aveslope' : 'AveSlope',
    'geom' : 'MULTIPOLYGON',
}

subwatersheds_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'psa_subwatersheds_4326.shp'))

surfacehydro_mapping = {
    'id' : 'Id',
    'geom' : 'MULTILINESTRING',
}
surfacehydro_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'tamaya', 'psa_surfacehydrology_4326.shp'))

# Soil layer mappings and shapefiles

soil_data_mapping = {
    'poly_id' : 'poly_id',
    'areasymbol' : 'AREASYMBOL',
    'spatialver' : 'SPATIALVER',
    'musym' : 'MUSYM',
    'mukey' : 'MUKEY',
    'mukey_1' : 'MUKEY_1',
    'tax_class' : 'tax_class',
    'org_matter' : 'org_matter',
    'composting' : 'composting',
    'texture' : 'texture',
    'ph_water' : 'ph_water',
    'bulk_densi' : 'bulk_densi',
    'geom' : 'POLYGON',
}

soil_data_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'tamaya_soil_data.shp'))

# LANDFIRE EVT MAPPINGS AND FILE

landfire_classes_mapping = {
    'value' : 'value',
    'label' : 'label',
}

landfire_legends = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'evt_legend.csv'))

def ag(verbose=True):
    ag_lm = LayerMapping(
        models.ag, ag_shp, ag_mapping,
        transform=False, encoding='iso-8859-1',
    )
    ag_lm.save(strict=True, verbose=verbose)

def vineyards(verbose=True):
    vn_lm = LayerMapping(
        models.vineyards, vineyards_shp, vineyards_mapping,
        transform=False, encoding='iso-8859-1',
    )
    vn_lm.save(strict=True, verbose=verbose)

def mbls(verbose=True):
    mbls_lm = LayerMapping(
        models.mbls, mbls_shp, mbls_mapping,
        transform=False, encoding='iso-8859-1',
    )
    mbls_lm.save(strict=True, verbose=verbose)

def run(verbose=True):

    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1',
    )
    boundary_lm.save(strict=True, verbose=verbose)

    buffered_bndry_lm = LayerMapping(
        models.buffered_bndry, buffered_bndry_shp, buffered_bndry_mapping,
        transform=False, encoding='iso-8859-1',
    )
    buffered_bndry_lm.save(strict=True, verbose=verbose)

    mbls_lm = LayerMapping(
        models.mbls, mbls_shp, mbls_mapping,
        transform=False, encoding='iso-8859-1',
    )
    mbls_lm.save(strict=True, verbose=verbose)

    roads_lm = LayerMapping(
        models.roads, roads_shp, roads_mapping,
        transform=False, encoding='iso-8859-1',
    )
    roads_lm.save(strict=True, verbose=verbose)

    watersheds_lm = LayerMapping(
        models.watersheds, watersheds_shp, watersheds_mapping,
        transform=False, encoding='iso-8859-1',
    )
    watersheds_lm.save(strict=True, verbose=verbose)

    subwatersheds_lm = LayerMapping(
        models.subwatersheds, subwatersheds_shp, subwatersheds_mapping,
        transform=False, encoding='iso-8859-1',
    )
    subwatersheds_lm.save(strict=True, verbose=verbose)

    surfacehydro_lm = LayerMapping(
        models.surfacehydro, surfacehydro_shp, surfacehydro_mapping,
        transform=False, encoding='iso-8859-1',
    )
    surfacehydro_lm.save(strict=True, verbose=verbose)


    soil_data_lm = LayerMapping(
        models.soil_data, soil_data_shp, soil_data_mapping,
        transform=False, encoding='iso-8859-1',
    )
    soil_data_lm.save(strict=True, verbose=verbose)

    landfire_classes_lm = LayerMapping(
        models.landfire_classes, landfire_legends, landfire_classes_mapping,
    )
    landfire_classes_lm.save(strict=True, verbose=verbose)
