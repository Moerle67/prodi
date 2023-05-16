
from django.contrib import admin

from .models import *

admin.site.register(Fachrichtung)
admin.site.register(Kostentraeger)
admin.site.register(Schlagwort)

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
   list_display = ['bezeichnung', 'partner', 'reserve']
   @admin.display()
   def partner(self, organisation):
      return f"{organisation.ansprechpartner}/{organisation.ansprechpartner_mail} Telefon: {organisation.ansprechpartner_telefon}"
   @admin.display()
   def reserve(self, organisation):
      return f"{organisation.ansprechpartner2}/{organisation.ansprechpartner2_mail} Telefon: {organisation.ansprechpartner2_telefon}"
      
@admin.register(Reha)
class RehaAdmin(admin.ModelAdmin):
   list_display = ['massnahmentitel', 'fachrichtung', 'organisation', 'status']
   search_fields = ['massnahmentitel', 'schlagwort__schlagwort']
   list_filter = ['kostentraeger', 'organisation', 'dauer','status', 'organisation', 'schlagwort']

