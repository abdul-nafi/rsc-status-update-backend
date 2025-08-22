from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import PartyMember

class PartyMemberResource(resources.ModelResource):
    class Meta:
        model = PartyMember
        import_id_fields = ('contact_number',)
        fields = (
            'name', 'contact_number', 'email', 'is_exited_country', 'is_on_vacation',
            'unit',  # <-- changed here from 'unit__name' to 'unit'
            'is_working', 'job_title'
        )

    def before_import_row(self, row, **kwargs):
        # Optional custom validation or processing before row import
        pass

@admin.register(PartyMember)
class PartyMemberAdmin(ImportExportModelAdmin):
    resource_class = PartyMemberResource
    list_display = ('name', 'contact_number', 'email', 'is_exited_country', 'is_on_vacation', 'unit', 'is_working', 'job_title', 'last_updated')
    search_fields = ('name', 'contact_number', 'email')
    list_filter = ('is_exited_country', 'is_on_vacation', 'is_working', 'unit')





