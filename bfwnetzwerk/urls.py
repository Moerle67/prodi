from django.urls import path
from django.contrib import admin

from . import views

admin.site.site_header  =  "BFW Angebotsübersicht Verwaltung"  
admin.site.site_title  =  "Side title"
admin.site.index_title  =  "Datenbanken"

urlpatterns = [
    path('form1', views.form1, name='index'),
    path('up_reha', views.upload_file_reha, name='upload_reha'),
    path('up_fari', views.upload_file_fari, name='upload_fari'),
    path('', admin.site.urls, name='admin'),
]