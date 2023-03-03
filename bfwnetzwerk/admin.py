
from django.contrib import admin

from .models import *

admin.site.register(Fachrichtung)
admin.site.register(Dokument)
admin.site.register(Kostentraeger)
@admin.register(Vorschlag)
class VorschlagAdmin(admin.ModelAdmin):
   def save_model(self, request, obj, form, change):
      obj = Vorschlag(obj)
      if not obj.user:
         obj.user = request.user
      obj.save()
@admin.register(Vorschlagbearbeitung)
class VorschlagbearbeitungAdmin(admin.ModelAdmin):
   def save_model(self, request, obj, form, change):
      obj = Vorschlagbearbeitung(obj)
      if not obj.user:
         obj.user = request.user    
      obj.save()
@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
   list_display = ['name', 'mail', 'telefon']

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
   list_display = ['bezeichnung', 'partner']
   @admin.display()
   def partner(self, obj):
      return f"{obj.ansprechpartner.name} -- {obj.ansprechpartner.mail} -- Telefon: {obj.ansprechpartner.telefon}"
@admin.register(Reha)
class RehaAdmin(admin.ModelAdmin):
   list_display = ['massnahmentitel', 'fachrichtung', 'organisation', 'verantwortlicher', 'status']
   search_fields = ['massnahmentitel', 'schlagrichtung', 'schlagwort']
   list_filter = ['schlagwort','kostentraeger', 'organisation', 'dauer', 'verantwortlicher','status']
   admin.site.register(Schlagwort)
