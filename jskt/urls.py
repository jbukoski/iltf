from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from . import views
from django.contrib.gis import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='jskt_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^boundary/', views.boundary_view, name='jskt_boundary'),
    url(r'^buff_bndry/', views.buff_bndry_view, name='jskt_buff_bndry'),
    url(r'^boundary_dl/', views.boundary_view_dl, name='jskt_boundary_dl'),
    #url(r'^bulk_dens_dl/', views.bd_dl_view, name='jskt_bulk_dens_dl'),
    #url(r'^landfire_dl/$', views.landfire_dl_view, name = 'landfire_dl'),
    #url(r'^ndvi_2005_dl/$', views.ndvi_2005_dl_view, name = 'ndvi_2005_dl'),
    #url(r'^ndvi_2010_dl/$', views.ndvi_2010_dl_view, name = 'ndvi_2010_dl'),
    #url(r'^ndvi_2015_dl/$', views.ndvi_2015_dl_view, name = 'ndvi_2015_dl'),
    #url(r'^agc_dl/$', views.agc_dl_view, name = 'agc_dl'),
    #url(r'^bgc_dl/$', views.bgc_dl_view, name = 'bgc_dl'),
    #url(r'^soc_dl/$', views.soc_dl_view, name = 'soc_dl'),
    url(r'^sample_up/', views.sample_up_view, name='jskt_sample_up'),
    url(r'^render_geojson/', views.render_geojson_view, name='render_geojson'),
    url(r'^download_single/', views.download_single_view, name="jskt_download_single"),
    url(r'^delete_single/', views.delete_single_view, name="jskt_delete_single"),
    url(r'^delete_up/', views.delete_up_view, name='jskt_delete_up'),
    url(r'^admin/logout/$', views.signout_view, name='signout'),
]
