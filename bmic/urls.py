from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
import calc.views
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='bmic_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^sample_up/', views.sample_up_view, name='sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name='download_single'),
    url(r'^delete_single/', views.delete_single_view, name='delete_single'),
    url(r'^delete_up/', views.delete_up_view, name='delete_up'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
    url(r'^aoc_mi_stmarys/', views.aoc_mi_stmarys_view, name = 'bmic_aoc_mi_stmarys'),
    url(r'^aoc_mi_stmarys_dl/', views.aoc_mi_stmarys_view_dl, name = 'bmic_aoc_mi_stmarys_dl'),
    url(r'^boundary/', views.boundary_view, name = 'bmic_boundary'),
    url(r'^boundary_dl/', views.boundary_view_dl, name = 'bmic_boundary_dl'),
    url(r'^buffered_bndry/', views.buffered_bndry_view, name = 'bmic_buffered_bndry'),
    url(r'^buffered_bndry_dl/', views.buffered_bndry_view_dl, name = 'bmic_buffered_bndry_dl'),
    url(r'^ceded_territory/', views.ceded_territory_view, name = 'bmic_ceded_territory'),
    url(r'^ceded_territory_dl/', views.ceded_territory_view_dl, name = 'bmic_ceded_territory_dl'),
    url(r'^chippewa_cnty/', views.chippewa_cnty_view, name = 'bmic_chippewa_cnty'),
    url(r'^chippewa_cnty_dl/', views.chippewa_cnty_view_dl, name = 'bmic_chippewa_cnty_dl'),
    url(r'^chippewa_roads/', views.chippewa_roads_view, name = 'bmic_chippewa_roads'),
    url(r'^chippewa_roads_dl/', views.chippewa_roads_view_dl, name = 'bmic_chippewa_roads_dl'),
    url(r'^chippewa_streams/', views.chippewa_streams_view, name = 'bmic_chippewa_streams'),
    url(r'^chippewa_streams_dl/', views.chippewa_streams_view_dl, name = 'bmic_chippewa_streams_dl'),
    url(r'^chippewa_waterwells/', views.chippewa_waterwells_view, name = 'bmic_chippewa_waterwells'),
    url(r'^chippewa_waterwells_dl/', views.chippewa_waterwells_view_dl, name = 'bmic_chippewa_waterwells_dl'),
    url(r'^coastal_wetlands/', views.coastal_wetlands_view, name = 'bmic_coastal_wetlands'),
    url(r'^coastal_wetlands_dl/', views.coastal_wetlands_view_dl, name = 'bmic_coastal_wetlands_dl'),
    url(r'^comm_forst_ceded/', views.comm_forst_ceded_view, name = 'bmic_comm_forst_ceded'),
    url(r'^comm_forst_ceded_dl/', views.comm_forst_ceded_view_dl, name = 'bmic_comm_forst_ceded_dl'),
    url(r'^critical_dunes/', views.critical_dunes_view, name = 'bmic_critical_dunes'),
    url(r'^critical_dunes_dl/', views.critical_dunes_view_dl, name = 'bmic_critical_dunes_dl'),
    url(r'^e_hiawathanf/', views.e_hiawathanf_view, name = 'bmic_e_hiawathanf'),
    url(r'^e_hiawathanf_dl/', views.e_hiawathanf_view_dl, name = 'bmic_e_hiawathanf_dl'),
    url(r'^eup_state_parks/', views.eup_state_parks_view, name = 'bmic_eup_state_parks'),
    url(r'^eup_state_parks_dl/', views.eup_state_parks_view_dl, name = 'bmic_eup_state_parks_dl'),
    url(r'^golf_course/', views.golf_course_view, name = 'bmic_golf_course'),
    url(r'^golf_course_dl/', views.golf_course_view_dl, name = 'bmic_golf_course_dl'),
    url(r'^great_lakes/', views.great_lakes_view, name = 'bmic_great_lakes'),
    url(r'^great_lakes_dl/', views.great_lakes_view_dl, name = 'bmic_great_lakes_dl'),
    url(r'^ir_roads/', views.ir_roads_view, name = 'bmic_ir_roads'),
    url(r'^ir_roads_dl/', views.ir_roads_view_dl, name = 'bmic_ir_roads_dl'),
    url(r'^lake_sprior_grid/', views.lake_sprior_grid_view, name = 'bmic_lake_sprior_grid'),
    url(r'^lake_sprior_grid_dl/', views.lake_sprior_grid_view_dl, name = 'bmic_lake_sprior_grid_dl'),
    url(r'^mi_cntys/', views.mi_cntys_view, name = 'bmic_mi_cntys'),
    url(r'^mi_cntys_dl/', views.mi_cntys_view_dl, name = 'bmic_mi_cntys_dl'),
    url(r'^mi_lakes/', views.mi_lakes_view, name = 'bmic_mi_lakes'),
    url(r'^mi_lakes_dl/', views.mi_lakes_view_dl, name = 'bmic_mi_lakes_dl'),
    url(r'^mi_state_parks/', views.mi_state_parks_view, name = 'bmic_mi_state_parks'),
    url(r'^mi_state_parks_dl/', views.mi_state_parks_view_dl, name = 'bmic_mi_state_parks_dl'),
    url(r'^parcels/', views.parcels_view, name = 'bmic_parcels'),
    url(r'^parcels_dl/', views.parcels_view_dl, name = 'bmic_parcels_dl'),
    url(r'^pwr_syst_backup_2014/', views.pwr_syst_backup_2014_view, name = 'bmic_pwr_syst_backup_2014'),
    url(r'^pwr_syst_backup_2014_dl/', views.pwr_syst_backup_2014_view_dl, name = 'bmic_pwr_syst_backup_2014_dl'),
    url(r'^railroad/', views.railroad_view, name = 'bmic_railroad'),
    url(r'^railroad_dl/', views.railroad_view_dl, name = 'bmic_railroad_dl'),
    url(r'^rivers/', views.rivers_view, name = 'bmic_rivers'),
    url(r'^rivers_dl/', views.rivers_view_dl, name = 'bmic_rivers_dl'),
    url(r'^snowmobile_trails/', views.snowmobile_trails_view, name = 'bmic_snowmobile_trails'),
    url(r'^snowmobile_trails_dl/', views.snowmobile_trails_view_dl, name = 'bmic_snowmobile_trails_dl'),
    url(r'^subwatersheds/', views.subwatersheds_view, name = 'bmic_subwatersheds'),
    url(r'^subwatersheds_dl/', views.subwatersheds_view_dl, name = 'bmic_subwatersheds_dl'),
    url(r'^waishkey_add_streams/', views.waishkey_add_streams_view, name = 'bmic_waishkey_add_streams'),
    url(r'^waishkey_add_streams_dl/', views.waishkey_add_streams_view_dl, name = 'bmic_waishkey_add_streams_dl'),
    url(r'^waishkey_ptnl_wtlnd_rstrn/', views.waishkey_ptnl_wtlnd_rstrn_view, name = 'bmic_waishkey_ptnl_wtlnd_rstrn'),
    url(r'^waishkey_ptnl_wtlnd_rstrn_dl/', views.waishkey_ptnl_wtlnd_rstrn_view_dl, name = 'bmic_waishkey_ptnl_wtlnd_rstrn_dl'),
    url(r'^waishkey_river/', views.waishkey_river_view, name = 'bmic_waishkey_river'),
    url(r'^waishkey_river_dl/', views.waishkey_river_view_dl, name = 'bmic_waishkey_river_dl'),
    url(r'^waiska_watershed/', views.waiska_watershed_view, name = 'bmic_waiska_watershed'),
    url(r'^waiska_watershed_dl/', views.waiska_watershed_view_dl, name = 'bmic_waiska_watershed_dl'),
    url(r'^wastewater_lines/', views.wastewater_lines_view, name = 'bmic_wastewater_lines'),
    url(r'^wastewater_lines_dl/', views.wastewater_lines_view_dl, name = 'bmic_wastewater_lines_dl'),
    url(r'^wellhead_protection/', views.wellhead_protection_view, name = 'bmic_wellhead_protection'),
    url(r'^wellhead_protection_dl/', views.wellhead_protection_view_dl, name = 'bmic_wellhead_protection_dl'),
    url(r'^wetland_preserve/', views.wetland_preserve_view, name = 'bmic_wetland_preserve'),
    url(r'^wetland_preserve_dl/', views.wetland_preserve_view_dl, name = 'bmic_wetland_preserve_dl'),
    url(r'^whitefish_bay_reserve/', views.whitefish_bay_reserve_view, name = 'bmic_whitefish_bay_reserve'),
    url(r'^whitefish_bay_reserve_dl/', views.whitefish_bay_reserve_view_dl, name = 'bmic_whitefish_bay_reserve_dl'),

]
