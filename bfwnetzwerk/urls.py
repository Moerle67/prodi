from django.urls import path
from django.contrib import admin

from . import views

admin.site.site_header  =  "Produktdatenbank BFW-Netzwerk"  
admin.site.site_title  =  "Side title"
admin.site.index_title  =  "Tabellen"

urlpatterns = [
    path('form1', views.form1, name='index'),
    path('up_prod', views.upload_file_prod, name='upload_prod'),
    # path('up_fari', views.upload_file_fari, name='upload_fari'),
    path('', admin.site.urls, name='admin'),
]