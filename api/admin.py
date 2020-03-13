from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from api.models import Data


@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_per_page = 50
    search_fields = ('date', 'channel', 'country', 'os')
    list_display = ('date', 'channel', 'country', 'os')
    list_filter = ('os', 'channel', 'country')
