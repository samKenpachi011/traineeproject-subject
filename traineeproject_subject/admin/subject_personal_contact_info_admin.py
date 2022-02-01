from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple
from ..admin_site import traineeproject_subject_admin
from .modeladmin_mixins import ModelAdminMixin
from ..models import PersonalContactInfo
from ..forms import PersonalContactInfoForm

@admin.register(PersonalContactInfo, site=traineeproject_subject_admin)
class PersonalContactInfoAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = PersonalContactInfoForm

    fieldsets = (
        (None,{
        'fields':[
                'subject_identifier',
                'report_datetime',
                'date_signed',
                'may_visit_home',
                'physical_address',
                'may_call',
                'subject_cell',
                'subject_cell_alt',
                'subject_phone',
                'subject_phone_alt',
                'may_call_work',
                'subject_work_place',
                'subject_work_phone',]
    }),(
        'Emergency Contact Details', {
            'fields': [
                'may_contact_indirectly',
                'indirect_contact_name',
                'indirect_contact_relation',
                'indirect_contact_physical_address',
                'indirect_contact_cell',
                'indirect_contact_phone',
            ],
        }),audit_fieldset_tuple)


    radio_fields = {'may_visit_home': admin.VERTICAL,
                'may_call': admin.VERTICAL,
                'may_call_work': admin.VERTICAL,
                'may_contact_indirectly': admin.VERTICAL, }

    search_fields = ('subject_identifier', )

    list_display = ('subject_identifier', 'may_visit_home', 'may_call',
                    'may_call_work')

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

