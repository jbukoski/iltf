from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models
from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json, os, os.path, psycopg2, re, time

from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError

# Specify downloads path
path = os.path.dirname(os.path.abspath(__file__))

@login_required(login_url='/login/')
def index(request):
     
    if not request.user.username == 'tamaya_user':
        return HttpResponseRedirect(reverse('iltf_index'))

    bndry = models.boundary.objects.all()
    documents = models.Document.objects.all()
    upload_files = next(os.walk(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded')))[2]
    upload_list = []

    for up_file in upload_files:

        if up_file != ".DS_Store":

            up_file_path = os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)
            raw_doc_json = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/', up_file)).read()
            upload_list.append(raw_doc_json)

    doc_counter = 1

    for document in documents:
        doc_counter += 1

    return render(request, 'tamaya/index.html', {
        'title': 'Santa Ana Pueblo of NM',
        'bndry': bndry,
        'documents': documents
    })

def home(request):
    return HttpResponseRedirect(urlresolvers.reverse('admin:app_list', args=("tamaya/",)))

def render_geojson_view(request):

    if request.method == 'POST':
        lyr = request.POST['layer']
        lyr_json = open(os.path.join(os.path.dirname(path), 'media', lyr), 'r+').read()

        return JsonResponse({'layer': lyr, 'layer_json': lyr_json})

    else:
        error_msg = 'Not a post request'

        return JsonResponse(error_msg, safe = False)

# Layers

def boundary_view(request):
    boundary_json = serialize('geojson', models.boundary.objects.all(), geometry_field="geom")
    return HttpResponse(boundary_json, content_type='json')

def buff_boundary_view(request):
    buff_boundary_json = serialize('geojson', models.buffered_bndry.objects.all(), geometry_field="geom")
    return HttpResponse(buff_boundary_json, content_type='json')

def ag_view(request):
    ag_json = serialize('geojson', models.ag.objects.all(), geometry_field="geom", fields=('id', 'acres', 'status', 'tract_numb', 'community', 'soctotal', 'socmean'))
    return HttpResponse(ag_json, content_type='json')

def vineyards_view(request):
    vineyards_json = serialize('geojson', models.vineyards.objects.all(), geometry_field="geom", fields=('section', 'acres', 'soctotal', 'socmean'))
    return HttpResponse(vineyards_json, content_type='json')

def mbls_view(request):
    mbls_json = serialize('geojson', models.mbls.objects.all(), geometry_field="geom", fields=('entity', 'area', 'acres', 'comment', 'perimeter', 'mbl_field', 'soctotal', 'socmean'))
    return HttpResponse(mbls_json, content_type='json')

def roads_view(request):
    roads_json = serialize('geojson', models.roads.objects.all(), geometry_field="geom", fields=('name', 'surface', 'comment', 'condition', 'id'))
    return HttpResponse(roads_json, content_type='json')

def watersheds_view(request):
    watersheds_json = serialize('geojson', models.watersheds.objects.all(), geometry_field="geom", fields=('watershed_id', 'hu_8_name', 'shape_area'))
    return HttpResponse(watersheds_json, content_type="json")

def subwatersheds_view(request):
    subwatersheds_json = serialize('geojson', models.subwatersheds.objects.all(), geometry_field="geom", fields=('subwatershed_id', 'watershed', 'subwatshed', 'acres'))
    return HttpResponse(subwatersheds_json, content_type="json")

def surfacehydro_view(request):
    surfacehydro_json = serialize('geojson', models.surfacehydro.objects.all(), geometry_field="geom")
    return HttpResponse(surfacehydro_json, content_type="json")

def soil_data_view(request):
    soil_data_json = serialize('geojson', models.soil_data.objects.all(), geometry_field="geom", fields=('poly_id','tax_class', 'org_matter', 'composting', 'texture', 'ph_water', 'bulk_densi'))
    return HttpResponse(soil_data_json, content_type='json')

###############
## Downloads ##
###############

# Admin layers

def boundary_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'boundary.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="boundary.zip"'

    return response

def ag_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'agriculture.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="agriculture.zip"'

    return response

def vineyards_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'vineyards.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="vineyards.zip"'

    return response

def mbl_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'mbl_int.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="mbl_int.zip"'

    return response

def roads_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'santa_ana_roads.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="reservation_roads.zip"'

    return response

# Hydrology layers

def watersheds_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'watersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="watersheds.zip"'

    return response

def subwatersheds_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'subwatersheds.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="subwatersheds.zip"'

    return response

def surfacehydrology_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'surfacehydrology.zip'), 'rb')
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="surfacehydrology.zip"'

    return response

# Soil layers

def bd_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'bulk_density_1_3_bar.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="bulk_density_1_3_bar.zip"'

    return response

def compost_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'composting_medium_and_final_cover.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="composting_medium_and_final_cover.zip"'

    return response

def om_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'organic_matter.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="organic_matter.zip"'

    return response

def ph_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'ph_surface_weighted_average.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="ph_surface_weighted_average.zip"'

    return response

def taxonomy_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'soil_taxonomy.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_taxonomy.zip"'

    return response

def texture_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'surface_texture_dcp.zip'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="soil_texture_dcp.zip"'

    return response

## Vegetation layers

def landfire_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_landfire_evt.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_landfire_evt.tif"'

    return response

def ndvi_2005_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2005.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2005.tif"'

    return response

def ndvi_2010_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2010.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2010.tif"'

    return response

def ndvi_2015_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_ndvi_2015.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_ndvi_2015.tif"'

    return response

## Carbon layers

def agc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_forest_agc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_forest_agc.tif"'

    return response

def bgc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_forest_bgc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_forest_bgc.tif"'

    return response

def soc_dl_view(request):
    download_file = open(os.path.join(os.path.dirname(path), 'data', 'tamaya', 'tamaya_gssurgo_soc.tif'), "rb")
    response = HttpResponse(download_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="tamaya_gssurgo_soc.tif"'

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

                download_file = open(os.path.join(os.path.dirname(path), 'media/tamaya/uploaded/boundary.geojson'), "rb")
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

                        download_file = open(os.path.join(os.path.dirname(path), "media/tamaya/uploaded/", short_name), "rb")
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

                file_path = os.path.join('tamaya/uploaded/', this_file.name)

                filename = re.sub('\.geojson$', '', this_file.name)

                newdoc = models.Document(docfile = request.FILES['docfile'], name=filename)
                newdoc.save()

                documents = models.Document.objects.all()

                return HttpResponseRedirect(reverse('tamaya_index'))

        return render(request, 'tamaya_index')

    else:
        form = DocumentForm()       # Empty

    # Load documents from the list page

    context = {'documents' : documents, 'form' : form}

    return render(request, 'tamaya_index', context)

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

        return HttpResponseRedirect(reverse('tamaya_index'))


def delete_up_view(request):

    i = 0
    documents = models.Document.objects.all()
    for document in documents:

        i += 1

        os.remove(os.path.join(settings.MEDIA_ROOT, document.docfile.name))
        document.delete()

    return HttpResponseRedirect(reverse('tamaya_index'))

# Logout

def signout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('iltf_index'))
