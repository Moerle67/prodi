
from django.contrib import admin

from .models import *

admin.site.register(Fachrichtung)
admin.site.register(Kontakt)
admin.site.register(Dokument)
admin.site.register(Organisation)
@admin.register(Reha)
class RehaAdmin(admin.ModelAdmin):
    list_display = ['massnahmentitel', 'fachrichtung', 'organisation', 'verantwortlicher', ]
    search_fields = ['massnahmentitel', 'schlagrichtung']
admin.site.register(Schlagwort)
admin.site.register(SchlagwortReha)

