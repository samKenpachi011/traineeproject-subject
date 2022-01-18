from django.contrib import admin
from ..models import SubjectDemographicsQuestionnaire
from ..forms import DemographicQuetionnaireForm
from ..admin_site import traineeproject_subject_admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from .modeladmin_mixins import CrfModelAdminMixin

@admin.register(SubjectDemographicsQuestionnaire, site=traineeproject_subject_admin)
class DemographicsQuestionnaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = DemographicQuetionnaireForm
    fieldsets = (
        (None, {          
            'fields':[
                'subject_visit',
                'report_datetime',
                'country',
                'ethnicity',
                'ethnicity_other',
                'household_members',
                'highest_education',
                'employment_status',
                'employment_status_other',
                'settlement_type',
                'marital_status',
                'marital_status_other',
                'running_water',
            ]}
            ),audit_fieldset_tuple
            )
    

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
