
from django.contrib import admin

from .models import *

admin.site.register(Fachrichtung)
admin.site.register(Kontakt)
admin.site.register(Dokument)
admin.site.register(Organisation)
admin.site.register(Kostentraeger)
@admin.register(Reha)
class RehaAdmin(admin.ModelAdmin):
   list_display = ['massnahmentitel', 'fachrichtung', 'organisation', 'verantwortlicher', ]
   search_fields = ['massnahmentitel', 'schlagrichtung']
   list_filter = ['schlagwort','kostentraeger']
   admin.site.register(Schlagwort)
