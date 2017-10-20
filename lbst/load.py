import os
from django.contrib.gis.utils import LayerMapping
from . import models

# Admin Layers

boundary_mapping = {
    'objectid' : 'OBJECTID',
    'own_type' : 'own_type',
    'own_name' : 'own_name',
    'mgr_name_d' : 'mgr_name_d',
    'p_des_tp' : 'p_des_tp',
    'p_loc_ds' : 'p_loc_ds',
    'p_des_nm' : 'p_des_nm',
    'p_loc_nm' : 'p_loc_nm',
    's_des_tp' : 's_des_tp',
    's_loc_ds' : 's_loc_ds',
    's_des_nm' : 's_des_nm',
    's_loc_nm' : 's_loc_nm',
    't_des_tp' : 't_des_tp',
    't_loc_ds' : 't_loc_ds',
    't_des_nm' : 't_des_nm',
    't_loc_nm' : 't_loc_nm',
    'state_nm' : 'state_nm',
    'gap_sts' : 'gap_sts',
    'iucn_cat' : 'iucn_cat',
    'gis_src' : 'gis_src',
    'src_date' : 'src_date',
    'comments' : 'comments',
    'gis_acres' : 'gis_acres',
    'status' : 'status',
    'fia_code' : 'FIA_code',
    'shape_leng' : 'Shape_Leng',
    'res_status' : 'Res_status',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'reservation_boundary.shp'))

counties_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'cnty_id' : 'ID',
    'id2' : 'ID2',
    'geo' : 'GEO',
    'target_geo' : 'TARGET_GEO',
    'target_g_1' : 'TARGET_G_1',
    'pop_total' : 'POP_TOTAL',
    'pop_hu' : 'POP_HU',
    'pop_occ_hu' : 'POP_OCC_HU',
    'pop_vac_hu' : 'POP_VAC_HU',
    'shape_area' : 'Shape_area',
    'shape_len' : 'Shape_len',
    'geom' : 'POLYGON',
}

counties_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'counties.shp'))


parcels_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'biglst_field' : 'BIGLST_',
    'biglst_id' : 'BIGLST_ID',
    'pls_town' : 'PLS_TOWN',
    'pls_range' : 'PLS_RANGE',
    'pls_sec' : 'PLS_SEC',
    'pls_pm' : 'PLS_PM',
    'lst_owntyp' : 'LST_OWNTYP',
    'lst_restyp' : 'LST_RESTYP',
    'lst_open' : 'LST_OPEN',
    'lst_tractn' : 'LST_TRACTN',
    'lst_suffix' : 'LST_SUFFIX',
    'lst_mtract' : 'LST_MTRACT',
    'lst_msuffi' : 'LST_MSUFFI',
    'lst_lot' : 'LST_LOT',
    'lst_area' : 'LST_AREA',
    'lst_sym' : 'LST_SYM',
    'acres' : 'ACRES',
    'owntype' : 'OWNTYPE',
    'owner' : 'OWNER',
    'own' : 'OWN',
    'num' : 'NUM',
    'geom' : 'MULTIPOLYGON',
}

parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'parcels.shp'))

new_purchases_mapping = {
    'objectid' : 'OBJECTID',
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'bigplsc_field' : 'BIGPLSC_',
    'bigplsc_id' : 'BIGPLSC_ID',
    'sec' : 'SEC',
    'town' : 'TOWN',
    'rng' : 'RNG',
    'mer' : 'MER',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'remarks' : 'remarks',
    'purch_name' : 'Purch_name',
    'purch_date' : 'Purch_date',
    'sect_t_r' : 'SECT_T_R',
    'legal_desc' : 'legal_desc',
    'acres_field' : 'ACRES_',
    'geom' : 'MULTIPOLYGON',
}

new_purchases_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'new_purchases.shp'))


# Wildlife Habitat Layers

food_plots_mapping = {
    'objectid' : 'OBJECTID',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'area' : 'AREA',
    'plot_numbe' : 'PLOT_NUMBE',
    'acres' : 'ACRES',
    'crop_2014' : 'CROP_2014',
    'crop_2015' : 'CROP_2015',
    'geom' : 'MULTIPOLYGON',
}

food_plots_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'food_plots.shp'))


grasslands_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'location' : 'LOCATION',
    'shape_area' : 'SHAPE_Area',
    'year_done' : 'YEAR_DONE',
    'acres' : 'ACRES',
    'cost' : 'COST',
    'geom' : 'MULTIPOLYGON',
}

grasslands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'grasslands_export.shp'))


habitat_leases_mapping = {
    'name' : 'NAME',
    'lease_or_p' : 'LEASE_OR_P',
    'start_date' : 'START_DATE',
    'end_date' : 'END_DATE',
    'annual_cos' : 'ANNUAL_COS',
    'total_acre' : 'TOTAL_ACRE',
    'payment_du' : 'PAYMENT_DU',
    'contract_l' : 'CONTRACT_L',
    'geom' : 'MULTIPOLYGON',
}

habitat_leases_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'HabitatLeases.shp'))


shelterbelts_mapping = {
    'objectid' : 'OBJECTID',
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'location' : 'LOCATION',
    'cost' : 'COST',
    'size_ac' : 'SIZE_AC',
    'number_of_field' : 'NUMBER_OF_',
    'year_done' : 'YEAR_DONE',
    'fabric_ft' : 'FABRIC_FT',
    'irrigated_field' : 'IRRIGATED_',
    'geom' : 'MULTIPOINT',
}

shelterbelts_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'homesite_shelterbelts.shp'))


trees_shrubs_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost_field' : 'COST____',
    'size_ac_field' : 'SIZE__AC_',
    'z_of_trees' : 'Z_OF_TREES',
    'year_done' : 'YEAR_DONE',
    'fabric_ft' : 'FABRIC__FT',
    'irrigated' : 'IRRIGATED',
    'geom' : 'MULTIPOLYGON',
}

trees_shrubs_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'trees_and_shrubs.shp'))


wetlands_mapping = {
    'operator' : 'OPERATOR',
    'program' : 'PROGRAM',
    'practice' : 'PRACTICE',
    'location' : 'LOCATION',
    'cost_field' : 'COST____',
    'size_ac_field' : 'SIZE__AC_',
    'year_done' : 'YEAR_DONE',
    'geom' : 'MULTIPOLYGON',
}

wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'wetlands.shp'))

# Carbon layers

c_avoided_conversion_mapping = {
    'id' : 'Id',
    'mgmt_unit' : 'Mgmt_Unit',
    'yr_establi' : 'Yr_Establi',
    'acres' : 'Acres',
    'fid_1' : 'FID_1',
    'id_1' : 'Id_1',
    'mgmt_uni_1' : 'Mgmt_Uni_1',
    'yr_estab_1' : 'Yr_Estab_1',
    'sixteen_yr' : 'Sixteen_Yr',
    'land_type' : 'Land_Type',
    'threat' : 'Threat',
    'acres_1' : 'Acres_1',
    'nrcs_pract' : 'NRCS_Pract',
    'peracreco2' : 'PerAcreCO2',
    'peryrtonsc' : 'perYrTonsC',
    'tons_co2e_field' : 'Tons_CO2e_',
    'geom' : 'POLYGON',
}

c_avoided_conversion_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'lbst', 'carbon_avoided_conversion.shp'))

def load_lyr(verbose=True):

    new_purchases_lm = LayerMapping(
        models.new_purchases, new_purchases_shp, new_purchases_mapping,
        transform=False, encoding='iso-8859-1'
    )
    new_purchases_lm.save(strict=True, verbose=verbose)

def run(verbose=True):

    # Admin layers

    boundary_lm  = LayerMapping(
        lbst_boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)


    counties_lm  = LayerMapping(
        models.counties, counties_shp, counties_mapping,
        transform=False, encoding='iso-8859-1'
    )
    counties_lm.save(strict=True, verbose=verbose)


    parcels_lm = LayerMapping(
        lbst_parcels, parcels_shp, parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    parcels_lm.save(strict=True, verbose=verbose)


    new_purchases_lm = LayerMapping(
        models.new_purchases, new_purchases_shp, new_purchases_mapping,
        transform=False, encoding='iso-8859-1'
    )
    new_purchases_lm.save(strict=True, verbose=verbose)


    food_plots_lm = LayerMapping(
        food_plots, food_plots_shp, food_plots_mapping,
        transform=False, encoding='iso-8859-1'
    )
    food_plots_lm.save(strict=True, verbose=verbose)


    grasslands_lm = LayerMapping(
        grasslands, grasslands_shp, grasslands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    grasslands_lm.save(strict=True, verbose=verbose)


    habitat_leases_lm = LayerMapping(
        habitat_leases, habitat_leases_shp, habitat_leases_mapping,
        transform=False, encoding='iso-8859-1',
    )
    habitat_leases_lm.save(strict=True, verbose=verbose)


    shelterbelts_lm = LayerMapping(
        shelterbelts, shelterbelts_shp, shelterbelts_mapping,
        transform=False, encoding='iso-8859-1',
    )
    shelterbelts_lm.save(strict=True, verbose=verbose)


    trees_shrubs_lm = LayerMapping(
        trees_shrubs, trees_shrubs_shp, trees_shrubs_mapping,
        transform=False, encoding='iso-8859-1',
    )
    trees_shrubs_lm.save(strict=True, verbose=verbose)

    wetlands_lm = LayerMapping(
        wetlands, wetlands_shp, wetlands_mapping,
        transform=False, encoding='iso-8859-1',
    )
    wetlands_lm.save(strict=True, verbose=verbose)

    c_avoided_conversion_lm = LayerMapping(
        models.c_avoided_conversion, c_avoided_conversion_shp, c_avoided_conversion_mapping,
        transform=False, encoding='iso-8859-1',
    )
    c_avoided_conversion_lm.save(strict=True, verbose=verbose)
