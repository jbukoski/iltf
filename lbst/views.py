from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import models
import json, os, os.path, psycopg2, re, time

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

#Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

@login_required(login_url='/login/')
def index(request):

    if not request.user.username == 'lbst_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/lbst/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/lbst/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/lbst/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'lbst/index.html', {
        'title': 'Lower Brule Sioux Tribe',
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("lbst/",)))


## Admin

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def buff_boundary_view(request):
    buff_boundary_json = serialize('geojson', models.buffered_bndry.objects.all(), geometry_field="geom")
    return HttpResponse(buff_boundary_json, content_type='json')

def counties_view(request):
    counties_json = serialize('geojson', models.counties.objects.all(), geometry_field="geom", fields=('namelsad10',))
    return HttpResponse(counties_json, content_type='json')

def parcels_view(request):
    parcels_json = serialize('geojson', models.parcels.objects.all(), geometry_field="geom", fields=('owntype', 'owner', 'acres'))
    return HttpResponse(parcels_json, content_type='json')

def new_purchases_view(request):
    new_purchases_json = serialize('geojson', models.new_purchases.objects.all(), geometry_field="geom", fields=('purch_name', 'purch_date', 'remarks', 'acres_field'))
    return HttpResponse(new_purchases_json, content_type='json')

## Habitats

def food_plots_view(request):
    food_plots_json = serialize('geojson', models.food_plots.objects.all(), geometry_field="geom", fields=('area', 'acres', 'crop_2014', 'crop_2015'))
    return HttpResponse(food_plots_json, content_type='json')

def grasslands_export_view(request):
    grasslands_export_json = serialize('geojson', models.grasslands_export.objects.all(), geometry_field="geom", fields=('operator', 'program', 'year_done', 'acres'))
    return HttpResponse(grasslands_export_json, content_type='json')

def habitat_leases_view(request):
    habitat_leases_json = serialize('geojson', models.habitat_leases.objects.all(), geometry_field="geom", fields=('name', 'start_date', 'end_date', 'total_acre'))
    return HttpResponse(habitat_leases_json, content_type='json')

def shelterbelts_view(request):
    shelterbelts_json = serialize('geojson', models.shelterbelts.objects.all(), geometry_field="geom", fields=('operator', 'program', 'year_done'))
    return HttpResponse(shelterbelts_json, content_type='json')

def trees_shrubs_view(request):
    trees_shrubs_json = serialize('geojson', models.trees_shrubs.objects.all(), geometry_field="geom", fields=('operator', 'program', 'practice', 'year_done'))
    return HttpResponse(trees_shrubs_json, content_type='json')

def wetlands_view(request):
    wetlands_json = serialize('geojson', models.wetlands.objects.all(), geometry_field="geom", fields=('operator', 'program', 'practice', 'year_done'))
    return HttpResponse(wetlands_json, content_type='json')

# Carbon layers

def c_avoided_view(request):
    c_avoided_json = serialize('geojson', models.c_avoided_conversion.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'acres_1', 'yr_estab_1', 'land_type', 'threat', 'nrcs_pract', 'peracreco2', 'peryrtonsc', 'tons_co2e_field'))
    return HttpResponse(c_avoided_json, content_type='json')

def c_food_plots_view(request):
    c_food_plots_json = serialize('geojson', models.c_food_plots.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'yr_estab_1', 'land_type', 'duration', 'sixteen_ye', 'acres_1', 'nrcs_pract', 'per_acre_c', 'per_year_t', 'tons_co2e_field', 'sixteen_1'))
    return HttpResponse(c_food_plots_json, content_type='json')

def c_native_grasslands_view(request):
    c_native_grasslands_json = serialize('geojson', models.c_native_grasslands.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'land_type', 'yr_estab_1', 'acres_1', 'nrcs_pract', 'peracreco2', 'peryrtonsc', 'assumed_si'))
    return HttpResponse(c_native_grasslands_json, content_type='json')

def c_new_grasslands_view(request):
    c_new_grasslands_json = serialize('geojson', models.c_new_grasslands.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'land_type', 'yr_estab_1', 'duration', 'sixteen_ye', 'acres_1', 'nrcs_pract', 'peracreco2', 'peryrtonsc', 'tonssincec', 'sisteen_1'))
    return HttpResponse(c_new_grasslands_json, content_type='json')

def c_new_treebelt_view(request):
    c_new_treebelt_json = serialize('geojson', models.c_new_treebelt.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'yr_estab_1', 'duration', 'sixteen_ye', 'acres_1', 'nrcs_pract', 'per_acre_c', 'per_yr_ton', 'tons_since', 'sixteen_1'))
    return HttpResponse(c_new_treebelt_json, content_type='json')

def c_old_treebelts_view(request):
    c_old_treebelts_json = serialize('geojson', models.c_old_treebelts.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'yr_estab_1', 'duration', 'sixteen_ye', 'acres_1', 'nrcs_pract', 'per_yr_ton', 'tons_since', 'sixteen_1'))
    return HttpResponse(c_old_treebelts_json, content_type='json')

def c_wetlands_view(request):
    c_wetlands_json = serialize('geojson', models.c_wetlands.objects.all(), geometry_field="geom", fields=('mgmt_uni_1', 'yr_estab_1', 'duration', 'sixteen_ye', 'acres_1', 'nrcs_pract', 'per_acre_c', 'per_yr_ton', 'tons_since', 'sixteen_1'))
    return HttpResponse(c_wetlands_json, content_type='json')

#########################
## Layer Download View ##
#########################

def boundary_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response

def counties_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'counties.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="counties.zip"'

    return response

def parcels_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'parcels.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="parcels.zip"'

    return response

def new_purchases_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'new_purchases.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="new_purchases.zip"'

    return response

def food_plots_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'foodplots.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="food_plots.zip"'

    return response

def grasslands_export_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'grasslandsexport.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="grasslands_export.zip"'

    return response

def habitat_leases_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'habitatleases.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="habitat_leases.zip"'

    return response

def shelterbelts_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'homesiteshelterbelts.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="shelterbelts.zip"'

    return response

def trees_shrubs_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'trees_and_shrubs.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="trees_and_shrubs.zip"'

    return response

def wetlands_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'wetlands.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="wetlands.zip"'

    return response

# Carbon download layers

def c_avoided_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_avoided_conversion.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_avoided_conversion.zip"'

    return response

def c_food_plots_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_food_plots.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_food_plots.zip"'

    return response

def c_native_grasslands_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_native_grasslands.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_native_grasslands.zip"'

    return response

def c_new_grasslands_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_new_grasslands.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_new_grasslands.zip"'

    return response

def c_new_treebelt_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_new_treebelt.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_new_treebelt.zip"'

    return response

def c_old_treebelts_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_old_treebelts.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_old_treebelts.zip"'

    return response

def c_wetlands_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'carbon_wetlands.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="carbon_wetlands.zip"'

    return response

# Raster layers

def evt_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'lbst_evt.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="lbst_evt.tif"'

    return response

def ndvi_2005_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', '2005_lbst_ndvi.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="2005_lbst_ndvi.tif"'

    return response

def ndvi_2010_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', '2010_lbst_ndvi.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="2010_lbst_ndvi.tif"'

    return response

def ndvi_2015_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', '2015_lbst_ndvi.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="2015_lbst_ndvi.tif"'

    return response

def agc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'lbst_agc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="lbst_agc.tif"'

    return response

def bgc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'lbst_bgc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="lbst_bgc.tif"'

    return response

def soc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'lbst', 'lbst_soc.tif'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="lbst_soc.tif"'

    return response

######################
## Import Utilities ##
######################

def sample_dl_view(request):

    try:
        if request.GET:

            print("request.GET: ", request.GET)

        elif request.POST:

            body_raw = request.body.decode("utf-8")
            end_file_name = len(body_raw)
            loc_file_name = body_raw.find("file_name")
            start_file_name = loc_file_name + 10        # where 'file_name=' starts + ends
            try_text_name = body_raw[start_file_name:end_file_name]
            text_name = try_text_name.replace("%2F", "/")

            if text_name == "boundary.geojson":

                download_file = open(os.path.join(os.path.dirname(path), 'media/lbst/uploaded/boundary.geojson'), "rb")
                response = HttpResponse(download_file, content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename="boundary.geojson"'
                return response

            else:

                all_docs = models.Document.objects.all()

                for document in all_docs:

                    foo_url = document.docfile.url
                    name_len = len(text_name)
                    short_name = text_name[16:name_len]

                    if document.docfile.name == text_name:

                        download_file = open(os.path.join(os.path.dirname(path), "media/lbst/uploaded/", short_name), "rb")
                        response = HttpResponse(download_file, content_type='application/force-download')
                        response['Content-Disposition'] = 'attachment; filename="' + short_name + '"'
                        return response

            download_file = open(os.path.join(os.path.dirname(path), document.docfile.url), "rb")
            response = HttpResponse(download_file, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="FAIL_FILE.sad"'
            return response
    except:

        print("\nError in request POST event\n")
        return HttpResponseRedirect(reverse('index'))

def sample_up_view(request):

    if request.method == 'GET':
        form = DocumentForm()

    elif request.method == 'POST':

        if request.FILES['docfile']:

            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():

                this_file = request.FILES['docfile']
                file_sys = FileSystemStorage()

                file_path = os.path.join('lbst/uploaded/', this_file.name)

                filename = re.sub('\.geojson$', '', this_file.name)

                newdoc = models.Document(docfile = request.FILES['docfile'], name=filename)
                newdoc.save()

                documents = models.Document.objects.all()

                return HttpResponseRedirect(reverse('lbst_index'))

        return render(request, 'lbst_index')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page

    context = {'documents' : documents, 'form' : form}

    return render(request, 'lbst_index', context)

def download_single_view(request):

    if request.method == "POST":

        file2download = request.POST['dl_file']

        download_file = open(os.path.join(os.path.dirname(path), 'media', file2download), "rb")
        response = HttpResponse(download_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="user_download.geojson"'

        return response

def delete_single_view(request):

    if request.method == "POST":

        file2delete = request.POST['dat']

        os.remove(os.path.join(settings.MEDIA_ROOT, file2delete))

        documents = models.Document.objects.all()
        doc2delete = documents.filter(docfile=file2delete)
        doc2delete.delete()

        return HttpResponseRedirect(reverse('lbst_index'))


def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()

    return HttpResponseRedirect(reverse('lbst_index'))

#################
## Logout View ##
#################

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))
