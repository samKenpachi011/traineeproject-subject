from django.contrib import admin

from ..forms import ScreeningEligibilityForm
from ..models import ScreeningEligibility
from ..admin_site import traineeproject_subject_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
@admin.register(ScreeningEligibility, site=traineeproject_subject_admin)
class ScreeningEligibilityAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ScreeningEligibilityForm
    fieldset = (
        (None, {
            'fields': ('age_in_years','is_guardian_present', 'gender',
             'nationality','married_to_citizen','proof_of_marriage',
            'is_literate','is_literate_witness_present'),

        }),
        audit_fieldset_tuple
        )

    search_fields = ('screening_identifier',)    
    readonly_fields = ('screening_identifier',)
    list_display = ('screening_identifier','age_in_years','is_eligible','reason_for_ineligibility','is_consented')

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)


    
    

  
