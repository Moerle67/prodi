
from django.contrib import admin

from .models import *

# admin.site.register(Organisation)
admin.site.register(Massnahmeart)
# admin.site.register(Schlagwort)
admin.site.register(Abrechnungsart)
admin.site.register(Kostentraeger)
# admin.site.register(Produkt)



@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
   list_display = ['bezeichnung', 'partner', 'reserve']
   @admin.display()
   def partner(self, organisation):
      return f"{organisation.ansprechpartner}/{organisation.ansprechpartner_mail} Telefon: {organisation.ansprechpartner_telefon}"
   @admin.display()
   def reserve(self, organisation):
      return f"{organisation.ansprechpartner2}/{organisation.ansprechpartner2_mail} Telefon: {organisation.ansprechpartner2_telefon}"
      
@admin.register(Produkt)
class RehaAdmin(admin.ModelAdmin):
    filter_horizontal = ['massnahmeart','schlagwoerter','kostentraeger','abrechnungsart','abschluss']
    list_display = ['massnahmentitel', 'schlagrichtung', 'organisation']
    search_fields = ['massnahmentitel', 'schlagwoerter__schlagwort', 'schlagrichtung']
    list_filter = ['organisation', 'massnahmeart', 'abrechnungsart']

@admin.register(Schlagwort)
class SchlagwortAdminAdmin(admin.ModelAdmin):      
   list_display = ['schlagwort']
   search_fields = ['schlagwort']

