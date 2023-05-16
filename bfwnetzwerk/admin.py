
from django.contrib import admin

from .models import *

admin.site.register(Fachrichtung)
admin.site.register(Kostentraeger)


# @admin.register(Organisation)
# class OrganisationAdmin(admin.ModelAdmin):
#    list_display = ['bezeichnung', 'partner']
#    @admin.display()
#    def partner(self, obj):
#       return f"{obj.ansprechpartner.name} -- {obj.ansprechpartner.mail} -- Telefon: {obj.ansprechpartner.telefon}"
      
@admin.register(Reha)
class RehaAdmin(admin.ModelAdmin):
   list_display = ['massnahmentitel', 'fachrichtung', 'organisation', 'verantwortlicher', 'status']
   search_fields = ['massnahmentitel', 'schlagrichtung', 'schlagwort']
   list_filter = ['kostentraeger', 'organisation', 'dauer', 'verantwortlicher','status', 'organisation','schlagwort']
   admin.site.register(Schlagwort)
