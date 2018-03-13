from django.urls import path

from . import views

app_name = 'search_satellite_images'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.get_download_info, name='info'),
    path('help/', views.get_help, name='help')
]