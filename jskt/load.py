import os
from django.contrib.gis.utils import LayerMapping
from . import models

all_prop_mapping = {
    'pnum' : 'PNUM',
    'version' : 'VERSION',
    'prop_id' : 'PROP_ID',
    'pacs_info' : 'PACS_INFO',
    'acres_gis' : 'ACRES_GIS',
    'acres_surv' : 'ACRES_SURV',
    'area_sf' : 'AREA_SF',
    'status' : 'STATUS',
    'prc_status' : 'PRC_STATUS',
    'owners' : 'OWNERS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'cdate' : 'CDATE',
    'edit_date' : 'EDIT_DATE',
    'mdoc_date' : 'MDOC_DATE',
    'mdoc_afn' : 'MDOC_AFN',
    'mdoc_typcd' : 'MDOC_TYPCD',
    'mdoc_type' : 'MDOC_TYPE',
    'vol' : 'VOL',
    'page' : 'PAGE',
    'lot' : 'LOT',
    'block' : 'BLOCK',
    'tideland' : 'TIDELAND',
    'tide_statu' : 'TIDE_STATU',
    'value_land' : 'VALUE_LAND',
    'value_impr' : 'VALUE_IMPR',
    'mkt_value' : 'MKT_VALUE',
    'luse_res' : 'LUSE_RES',
    'ludesc_res' : 'LUDESC_RES',
    'acres_res' : 'ACRES_RES',
    'luse_os' : 'LUSE_OS',
    'ludesc_os' : 'LUDESC_OS',
    'acres_os' : 'ACRES_OS',
    'luse_oth' : 'LUSE_OTH',
    'ludesc_oth' : 'LUDESC_OTH',
    'acres_oth' : 'ACRES_OTH',
    'value_res' : 'VALUE_RES',
    'value_os' : 'VALUE_OS',
    'value_oth' : 'VALUE_OTH',
    'prc_class' : 'PRC_CLASS',
    'rgn' : 'RGN',
    'region' : 'REGION',
    'sub_region' : 'SUB_REGION',
    'zoning' : 'ZONING',
    'zon_pct' : 'ZON_PCT',
    'zon_rmd' : 'ZON_RMD',
    'city' : 'CITY',
    'zip_code' : 'ZIP_CODE',
    'uga' : 'UGA',
    'lamird' : 'LAMIRD',
    'tax_area' : 'TAX_AREA',
    'levy' : 'LEVY',
    'fire_dist' : 'FIRE_DIST',
    'school' : 'SCHOOL',
    'mra' : 'MRA',
    'wr_code' : 'WR_CODE',
    'pwsid' : 'PWSID',
    'pws_group' : 'PWS_GROUP',
    'irrig' : 'IRRIG',
    'rts' : 'RTS',
    'qp' : 'QP',
    'label' : 'LABEL',
    'geo_12' : 'GEO_12',
    'pn12' : 'PN12',
    'rdate' : 'RDATE',
    'rdoc_afn' : 'RDOC_AFN',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'sort_by' : 'Sort_by',
    'ownership' : 'Ownership',
    'owner_nm' : 'Owner_nm',
    'owner_addr' : 'Owner_addr',
    'owner_city' : 'Owner_city',
    'owner_st' : 'Owner_ST',
    'owner_zip' : 'Owner_Zip',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'trust_num' : 'Trust_num',
    'survey' : 'Survey',
    'comments' : 'Comments',
    'year_purch' : 'Year_Purch',
    'site_work' : 'Site_work',
    'inventory' : 'Inventory',
    'explana_field' : 'Explana_',
    'trust_da' : 'Trust_Da',
    'perimeter' : 'Perimeter',
    'area' : 'Area',
    'acres' : 'Acres',
    'reser_num' : 'Reser_Num',
    'rentaltype' : 'RentalType',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

all_prop_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'all_prop.shp'))

boundary_mapping = {
    'aiannhce' : 'AIANNHCE',
    'aiannhns' : 'AIANNHNS',
    'affgeoid' : 'AFFGEOID',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'geom' : 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'boundary.shp'))

buff_bndry_mapping = {
    'objectid' : 'OBJECTID',
    'geom' : 'MULTIPOLYGON',
}

buff_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'buff_bndry.shp'))

cl_co_prop_db_mapping = {
    'pnum' : 'PNUM',
    'prop_id' : 'PROP_ID',
    'acres_gis' : 'ACRES_GIS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'zip_code' : 'ZIP_CODE',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'ownership' : 'Ownership',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

cl_co_prop_db_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'cl_co_prop_db.shp'))

counties_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'NAME',
    'state_name' : 'STATE_NAME',
    'state_fips' : 'STATE_FIPS',
    'cnty_fips' : 'CNTY_FIPS',
    'fips' : 'FIPS',
    'population' : 'POPULATION',
    'pop_sqmi' : 'POP_SQMI',
    'pop2010' : 'POP2010',
    'pop10_sqmi' : 'POP10_SQMI',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'ameri_es' : 'AMERI_ES',
    'asian' : 'ASIAN',
    'hawn_pi' : 'HAWN_PI',
    'hispanic' : 'HISPANIC',
    'other' : 'OTHER',
    'mult_race' : 'MULT_RACE',
    'males' : 'MALES',
    'females' : 'FEMALES',
    'age_under5' : 'AGE_UNDER5',
    'age_5_9' : 'AGE_5_9',
    'age_10_14' : 'AGE_10_14',
    'age_15_19' : 'AGE_15_19',
    'age_20_24' : 'AGE_20_24',
    'age_25_34' : 'AGE_25_34',
    'age_35_44' : 'AGE_35_44',
    'age_45_54' : 'AGE_45_54',
    'age_55_64' : 'AGE_55_64',
    'age_65_74' : 'AGE_65_74',
    'age_75_84' : 'AGE_75_84',
    'age_85_up' : 'AGE_85_UP',
    'med_age' : 'MED_AGE',
    'med_age_m' : 'MED_AGE_M',
    'med_age_f' : 'MED_AGE_F',
    'households' : 'HOUSEHOLDS',
    'ave_hh_sz' : 'AVE_HH_SZ',
    'hsehld_1_m' : 'HSEHLD_1_M',
    'hsehld_1_f' : 'HSEHLD_1_F',
    'marhh_chd' : 'MARHH_CHD',
    'marhh_no_c' : 'MARHH_NO_C',
    'mhh_child' : 'MHH_CHILD',
    'fhh_child' : 'FHH_CHILD',
    'families' : 'FAMILIES',
    'ave_fam_sz' : 'AVE_FAM_SZ',
    'hse_units' : 'HSE_UNITS',
    'vacant' : 'VACANT',
    'owner_occ' : 'OWNER_OCC',
    'renter_occ' : 'RENTER_OCC',
    'no_farms12' : 'NO_FARMS12',
    'ave_size12' : 'AVE_SIZE12',
    'crop_acr12' : 'CROP_ACR12',
    'ave_sale12' : 'AVE_SALE12',
    'sqmi' : 'SQMI',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

counties_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'counties.shp'))

fee_trust_mapping = {
    'pnum' : 'PNUM',
    'version' : 'VERSION',
    'prop_id' : 'PROP_ID',
    'pacs_info' : 'PACS_INFO',
    'acres_gis' : 'ACRES_GIS',
    'acres_surv' : 'ACRES_SURV',
    'area_sf' : 'AREA_SF',
    'status' : 'STATUS',
    'prc_status' : 'PRC_STATUS',
    'owners' : 'OWNERS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'cdate' : 'CDATE',
    'edit_date' : 'EDIT_DATE',
    'mdoc_date' : 'MDOC_DATE',
    'mdoc_afn' : 'MDOC_AFN',
    'mdoc_typcd' : 'MDOC_TYPCD',
    'mdoc_type' : 'MDOC_TYPE',
    'vol' : 'VOL',
    'page' : 'PAGE',
    'lot' : 'LOT',
    'block' : 'BLOCK',
    'tideland' : 'TIDELAND',
    'tide_statu' : 'TIDE_STATU',
    'value_land' : 'VALUE_LAND',
    'value_impr' : 'VALUE_IMPR',
    'mkt_value' : 'MKT_VALUE',
    'luse_res' : 'LUSE_RES',
    'ludesc_res' : 'LUDESC_RES',
    'acres_res' : 'ACRES_RES',
    'luse_os' : 'LUSE_OS',
    'ludesc_os' : 'LUDESC_OS',
    'acres_os' : 'ACRES_OS',
    'luse_oth' : 'LUSE_OTH',
    'ludesc_oth' : 'LUDESC_OTH',
    'acres_oth' : 'ACRES_OTH',
    'value_res' : 'VALUE_RES',
    'value_os' : 'VALUE_OS',
    'value_oth' : 'VALUE_OTH',
    'prc_class' : 'PRC_CLASS',
    'rgn' : 'RGN',
    'region' : 'REGION',
    'sub_region' : 'SUB_REGION',
    'zoning' : 'ZONING',
    'zon_pct' : 'ZON_PCT',
    'zon_rmd' : 'ZON_RMD',
    'city' : 'CITY',
    'zip_code' : 'ZIP_CODE',
    'uga' : 'UGA',
    'lamird' : 'LAMIRD',
    'tax_area' : 'TAX_AREA',
    'levy' : 'LEVY',
    'fire_dist' : 'FIRE_DIST',
    'school' : 'SCHOOL',
    'mra' : 'MRA',
    'wr_code' : 'WR_CODE',
    'pwsid' : 'PWSID',
    'pws_group' : 'PWS_GROUP',
    'irrig' : 'IRRIG',
    'rts' : 'RTS',
    'qp' : 'QP',
    'label' : 'LABEL',
    'geo_12' : 'GEO_12',
    'pn12' : 'PN12',
    'rdate' : 'RDATE',
    'rdoc_afn' : 'RDOC_AFN',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'sort_by' : 'Sort_by',
    'ownership' : 'Ownership',
    'owner_nm' : 'Owner_nm',
    'owner_addr' : 'Owner_addr',
    'owner_city' : 'Owner_city',
    'owner_st' : 'Owner_ST',
    'owner_zip' : 'Owner_Zip',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'trust_num' : 'Trust_num',
    'survey' : 'Survey',
    'comments' : 'Comments',
    'year_purch' : 'Year_Purch',
    'site_work' : 'Site_work',
    'inventory' : 'Inventory',
    'explana_field' : 'Explana_',
    'trust_da' : 'Trust_Da',
    'perimeter' : 'Perimeter',
    'area' : 'Area',
    'acres' : 'Acres',
    'reser_num' : 'Reser_Num',
    'rentaltype' : 'RentalType',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

fee_trust_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'fee_trust.shp'))

jef_co_prop_db_mapping = {
    'pin' : 'PIN',
    'pin_string' : 'PIN_STRING',
    'prop_id' : 'Prop_ID',
    'township' : 'Township',
    'range' : 'Range',
    'section_field' : 'Section_',
    'qtr_sectio' : 'Qtr_Sectio',
    'situs_addr' : 'Situs_Addr',
    'situs_city' : 'Situs_City',
    'situs_zip' : 'Situs_Zip',
    'owner' : 'Owner',
    'status' : 'Status',
    'prev_own' : 'Prev_own',
    'acres' : 'Acres',
    'tribal' : 'Tribal',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

jef_co_prop_db_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'jef_co_prop_db.shp'))

land_consolidation_mapping = {
    'fid_pttown' : 'FID_pttown',
    'data' : 'DATA',
    'fid_servic' : 'FID_servic',
    'id' : 'ID',
    'area' : 'Area',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

land_consolidation_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'land_consolidation.shp'))

prop_only_mapping = {
    'objectid' : 'OBJECTID',
    'pin' : 'PIN',
    'pin_string' : 'PIN_STRING',
    'land_use' : 'Land_Use',
    'lu_desc' : 'LU_Desc',
    'prop_id' : 'Prop_ID',
    'av_year' : 'AV_Year',
    'owner_id' : 'Owner_ID',
    'owner_name' : 'Owner_Name',
    'state_code' : 'State_Code',
    'tax_code' : 'Tax_Code',
    'school_dis' : 'School_Dis',
    'fire_dist' : 'Fire_Dist',
    'planning_a' : 'Planning_A',
    'ttl_acres' : 'Ttl_Acres',
    'legal_desc' : 'Legal_Desc',
    'cycle' : 'Cycle',
    'hood_code' : 'Hood_Code',
    'hood_desc' : 'Hood_Desc',
    'subdv_code' : 'Subdv_Code',
    'subdv_desc' : 'Subdv_Desc',
    'township' : 'Township',
    'range' : 'Range',
    'section_field' : 'Section_',
    'qtr_sectio' : 'Qtr_Sectio',
    'situs_addr' : 'Situs_Addr',
    'situs_city' : 'Situs_City',
    'situs_zip' : 'Situs_Zip',
    'certifiedf' : 'CertifiedF',
    'cfmv_imps' : 'CFMV_Imps',
    'cfmv_land' : 'CFMV_Land',
    'cfmv_total' : 'CFMV_Total',
    'notes' : 'Notes',
    'sale_reet' : 'Sale_Reet',
    'sale_deed' : 'Sale_Deed',
    'sale_price' : 'Sale_Price',
    'sale_date' : 'Sale_Date',
    'sale_multi' : 'Sale_Multi',
    'sale_rcode' : 'Sale_RCode',
    'sale_rdesc' : 'Sale_RDesc',
    'down_date' : 'Down_Date',
    'buildingph' : 'BuildingPh',
    'globalid' : 'GlobalID',
    'pacsweb_ye' : 'PACSWeb_Ye',
    'shapearea' : 'SHAPEarea',
    'shapelen' : 'SHAPElen',
    'owner' : 'Owner',
    'status' : 'Status',
    'prev_own' : 'Prev_own',
    'sort_by' : 'Sort_by',
    'perimeter' : 'Perimeter',
    'area' : 'Area',
    'acres' : 'Acres',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

prop_only_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'prop_only.shp'))

res_trust_mapping = {
    'pnum' : 'PNUM',
    'version' : 'VERSION',
    'prop_id' : 'PROP_ID',
    'pacs_info' : 'PACS_INFO',
    'acres_gis' : 'ACRES_GIS',
    'acres_surv' : 'ACRES_SURV',
    'area_sf' : 'AREA_SF',
    'status' : 'STATUS',
    'prc_status' : 'PRC_STATUS',
    'owners' : 'OWNERS',
    'situs_addr' : 'SITUS_ADDR',
    'situs_dir' : 'SITUS_DIR',
    'situs_rd' : 'SITUS_RD',
    'situs_ext' : 'SITUS_EXT',
    'situs_city' : 'SITUS_CITY',
    'cdate' : 'CDATE',
    'edit_date' : 'EDIT_DATE',
    'mdoc_date' : 'MDOC_DATE',
    'mdoc_afn' : 'MDOC_AFN',
    'mdoc_typcd' : 'MDOC_TYPCD',
    'mdoc_type' : 'MDOC_TYPE',
    'vol' : 'VOL',
    'page' : 'PAGE',
    'lot' : 'LOT',
    'block' : 'BLOCK',
    'tideland' : 'TIDELAND',
    'tide_statu' : 'TIDE_STATU',
    'value_land' : 'VALUE_LAND',
    'value_impr' : 'VALUE_IMPR',
    'mkt_value' : 'MKT_VALUE',
    'luse_res' : 'LUSE_RES',
    'ludesc_res' : 'LUDESC_RES',
    'acres_res' : 'ACRES_RES',
    'luse_os' : 'LUSE_OS',
    'ludesc_os' : 'LUDESC_OS',
    'acres_os' : 'ACRES_OS',
    'luse_oth' : 'LUSE_OTH',
    'ludesc_oth' : 'LUDESC_OTH',
    'acres_oth' : 'ACRES_OTH',
    'value_res' : 'VALUE_RES',
    'value_os' : 'VALUE_OS',
    'value_oth' : 'VALUE_OTH',
    'prc_class' : 'PRC_CLASS',
    'rgn' : 'RGN',
    'region' : 'REGION',
    'sub_region' : 'SUB_REGION',
    'zoning' : 'ZONING',
    'zon_pct' : 'ZON_PCT',
    'zon_rmd' : 'ZON_RMD',
    'city' : 'CITY',
    'zip_code' : 'ZIP_CODE',
    'uga' : 'UGA',
    'lamird' : 'LAMIRD',
    'tax_area' : 'TAX_AREA',
    'levy' : 'LEVY',
    'fire_dist' : 'FIRE_DIST',
    'school' : 'SCHOOL',
    'mra' : 'MRA',
    'wr_code' : 'WR_CODE',
    'pwsid' : 'PWSID',
    'pws_group' : 'PWS_GROUP',
    'irrig' : 'IRRIG',
    'rts' : 'RTS',
    'qp' : 'QP',
    'label' : 'LABEL',
    'geo_12' : 'GEO_12',
    'pn12' : 'PN12',
    'rdate' : 'RDATE',
    'rdoc_afn' : 'RDOC_AFN',
    'pacs_link' : 'PACS_LINK',
    'pmt_link' : 'PMT_LINK',
    'tribal' : 'Tribal',
    'sort_by' : 'Sort_by',
    'ownership' : 'Ownership',
    'owner_nm' : 'Owner_nm',
    'owner_addr' : 'Owner_addr',
    'owner_city' : 'Owner_city',
    'owner_st' : 'Owner_ST',
    'owner_zip' : 'Owner_Zip',
    'jskt_statu' : 'JSKT_statu',
    'prev_owner' : 'Prev_owner',
    'trust_num' : 'Trust_num',
    'survey' : 'Survey',
    'comments' : 'Comments',
    'year_purch' : 'Year_Purch',
    'site_work' : 'Site_work',
    'inventory' : 'Inventory',
    'explana_field' : 'Explana_',
    'trust_da' : 'Trust_Da',
    'perimeter' : 'Perimeter',
    'area' : 'Area',
    'acres' : 'Acres',
    'reser_num' : 'Reser_Num',
    'rentaltype' : 'RentalType',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

res_trust_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'res_trust.shp'))

service_area_mapping = {
    'fid_pttown' : 'FID_pttown',
    'data' : 'DATA',
    'fid_servic' : 'FID_servic',
    'id' : 'ID',
    'area' : 'Area',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

service_area_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'jskt', 'service_area.shp'))

def run_db(verbose=True):

    cl_co_prop_db_lm = LayerMapping(
        models.cl_co_prop_db, cl_co_prop_db_shp, cl_co_prop_db_mapping,
        transform=False, encoding='iso-8859-1'
    )
    cl_co_prop_db_lm.save(strict=True, verbose=verbose)

    jef_co_prop_db_lm = LayerMapping(
        models.jef_co_prop_db, jef_co_prop_db_shp, jef_co_prop_db_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jef_co_prop_db_lm.save(strict=True, verbose=verbose)


def run(verbose=True):

    all_prop_lm = LayerMapping(
        models.all_prop, all_prop_shp, all_prop_mapping,
        transform=False, encoding='iso-8859-1'
    )
    all_prop_lm.save(strict=True, verbose=verbose)

    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)

    buff_bndry_lm = LayerMapping(
        models.buff_bndry, buff_bndry_shp, buff_bndry_mapping,
        transform=False, encoding='iso-8859-1'
    )
    buff_bndry_lm.save(strict=True, verbose=verbose)

    cl_co_prop_db_lm = LayerMapping(
        models.cl_co_prop_db, cl_co_prop_db_shp, cl_co_prop_db_mapping,
        transform=False, encoding='iso-8859-1'
    )
    cl_co_prop_db_lm.save(strict=True, verbose=verbose)

    counties_lm = LayerMapping(
        models.counties, counties_shp, counties_mapping,
        transform=False, encoding='iso-8859-1'
    )
    counties_lm.save(strict=True, verbose=verbose)

    fee_trust_lm = LayerMapping(
        models.fee_trust, fee_trust_shp, fee_trust_mapping,
        transform=False, encoding='iso-8859-1'
    )
    fee_trust_lm.save(strict=True, verbose=verbose)

    jef_co_prop_db_lm = LayerMapping(
        models.jef_co_prop_db, jef_co_prop_db_shp, jef_co_prop_db_mapping,
        transform=False, encoding='iso-8859-1'
    )
    jef_co_prop_db_lm.save(strict=True, verbose=verbose)

    land_consolidation_lm = LayerMapping(
        models.land_consolidation, land_consolidation_shp, land_consolidation_mapping,
        transform=False, encoding='iso-8859-1'
    )
    land_consolidation_lm.save(strict=True, verbose=verbose)

    prop_only_lm = LayerMapping(
        models.prop_only, prop_only_shp, prop_only_mapping,
        transform=False, encoding='iso-8859-1'
    )
    prop_only_lm.save(strict=True, verbose=verbose)

    res_trust_lm = LayerMapping(
        models.res_trust, res_trust_shp, res_trust_mapping,
        transform=False, encoding='iso-8859-1'
    )
    res_trust_lm.save(strict=True, verbose=verbose)

    service_area_lm = LayerMapping(
        models.service_area, service_area_shp, service_area_mapping,
        transform=False, encoding='iso-8859-1'
    )
    service_area_lm.save(strict=True, verbose=verbose)
