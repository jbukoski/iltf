from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

import calc.views

urlpatterns = [
    url(r'^$', views.index, name='lbst_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='lbst_boundary'),
    url(r'^boundary_dl/', views.boundary_dl_view, name='lbst_boundary_dl'),
    url(r'^buff_bndry/', views.buff_boundary_view, name='lbst_buff_bndry'),
    url(r'^counties/', views.counties_view, name='lbst_counties'),
    url(r'^counties_dl/', views.counties_dl_view, name='lbst_counties_dl'),
    url(r'^parcels/', views.parcels_view, name='lbst_parcels'),
    url(r'^parcels_dl/', views.parcels_dl_view, name='lbst_parcels_dl'),
    url(r'^new_purchases/', views.new_purchases_view, name='lbst_new_purchases'),
    url(r'^new_purchases_dl/', views.new_purchases_dl_view, name='lbst_new_purchases_dl'),
    url(r'^food_plots/', views.food_plots_view, name='lbst_food_plots'),
    url(r'^food_plots_dl/', views.food_plots_dl_view, name='lbst_food_plots_dl'),
    url(r'^grasslands/', views.grasslands_export_view, name='lbst_grasslands_export'),
    url(r'^grasslands_export_dl/', views.grasslands_export_dl_view, name='lbst_grasslands_export_dl'),
    url(r'^habitat_leases/', views.habitat_leases_view, name='lbst_habitat_leases'),
    url(r'^habitat_leases_dl/', views.habitat_leases_dl_view, name='lbst_habitat_leases_dl'),
    url(r'^shelterbelts/', views.shelterbelts_view, name='lbst_shelterbelts'),
    url(r'^shelterbelts_dl/', views.shelterbelts_dl_view, name='lbst_shelterbelts_dl'),
    url(r'^trees_shrubs/', views.trees_shrubs_view, name='lbst_trees_shrubs'),
    url(r'^trees_shrubs_dl/', views.trees_shrubs_dl_view, name='lbst_trees_shrubs_dl'),
    url(r'^wetlands/', views.wetlands_view, name='lbst_wetlands'),
    url(r'^wetlands_dl/', views.wetlands_dl_view, name='lbst_wetlands_dl'),
    url(r'^c_avoided/', views.c_avoided_view, name='lbst_c_avoided'),
    url(r'^c_avoided_dl/', views.c_avoided_dl_view, name='lbst_c_avoided_dl'),
    url(r'^c_food_plots/', views.c_food_plots_view, name='lbst_c_food_plots'),
    url(r'^c_food_plots_dl/', views.c_food_plots_dl_view, name='lbst_c_food_plots_dl'),
    url(r'^c_native_grasslands/', views.c_native_grasslands_view, name='lbst_c_native_grasslands'),
    url(r'^c_native_grasslands_dl/', views.c_native_grasslands_dl_view, name='lbst_c_native_grasslands_dl'),
    url(r'^c_new_grasslands/', views.c_new_grasslands_view, name='lbst_c_new_grasslands'),
    url(r'^c_new_grasslands_dl/', views.c_new_grasslands_dl_view, name='lbst_c_new_grasslands_dl'),
    url(r'^c_new_treebelt/', views.c_new_treebelt_view, name='lbst_c_new_treebelt'),
    url(r'^c_new_treebelt_dl/', views.c_new_treebelt_dl_view, name='lbst_c_new_treebelt_dl'),
    url(r'^c_old_treebelts/', views.c_old_treebelts_view, name='lbst_c_old_treebelts'),
    url(r'^c_old_treebelts_dl/', views.c_old_treebelts_dl_view, name='lbst_c_old_treebelts_dl'),
    url(r'^c_wetlands/', views.c_wetlands_view, name='lbst_c_wetlands'),
    url(r'^c_wetlands_dl/', views.c_wetlands_dl_view, name='lbst_c_wetlands_dl'),
    url(r'^evt_dl/', views.evt_dl_view, name='lbst_evt_dl'),
    url(r'^2005_ndvi_dl/', views.ndvi_2005_dl_view, name='lbst_2005_ndvi_dl'),
    url(r'^2010_ndvi_dl/', views.ndvi_2010_dl_view, name='lbst_2010_ndvi_dl'),
    url(r'^2015_ndvi_dl/', views.ndvi_2015_dl_view, name='lbst_2015_ndvi_dl'),
    url(r'^agc_dl/', views.agc_dl_view, name='lbst_agc_dl'),
    url(r'^bgc_dl/', views.bgc_dl_view, name='lbst_bgc_dl'),
    url(r'^soc_dl/', views.soc_dl_view, name='lbst_soc_dl'),
    url(r'^sample_up/', views.sample_up_view, name='lbst_sample_up'),
    url(r'^delete_single/', views.delete_single_view, name="lbst_delete_single"),
    url(r'^download_single/', views.download_single_view, name="lbst_download_single"),
    url(r'^delete_up/', views.delete_up_view, name='lbst_delete_up'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]

