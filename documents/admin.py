from django.contrib import admin
from documents.models import Undertaker, Document


class DocumentAdmin(admin.ModelAdmin):
    date_hierarchy = 'reception_date'
    list_display = ('reception_serial', 'title', 'transmission_serial', 'summary')
    list_filter = ('undertaker__name',)
    ordering = ('-reception_serial',)

admin.site.register(Undertaker)
admin.site.register(Document, DocumentAdmin)
