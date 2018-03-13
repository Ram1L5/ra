from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import satsearch, json

# Create your views here.
def index(request):
    return render(request, 'search_satellite_images/index.html')

def get_download_info(request):
    params = {'path': request.POST.get('path'), 'row': request.POST.get('row'),
              'satellite_name': request.POST.get('satellite_name'), 'intersects': request.POST.get('intersects'),
              'date_from': request.POST.get('date_from'), 'date_to': request.POST.get('date_to'),
              'cloud_to': request.POST.get('cloud_to')}
    params = {k: v for k, v in params.items() if v}
    s = satsearch.Search(**params)
    scenes = satsearch.Scenes(s.scenes())
    geojson = json.dumps(scenes.geojson())
    geojson_fixed = json.loads(geojson.replace('null', '"no information"'))
    return render(request, 'search_info.html', {'info': geojson_fixed, 'params':params})

def get_help(request):
    return render(request, 'search_satellite_images/help.html')





