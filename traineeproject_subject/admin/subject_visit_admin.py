from django.contrib import admin
from django.contrib.admin.sites import site
from ..admin_site import traineeproject_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectVisit
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_model_admin import audit_fieldset_tuple
# from .modeladmin_mixins import ModelAdminMixin
@admin.register(SubjectVisit, site=traineeproject_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin,admin.ModelAdmin):
    form = SubjectVisitForm
    fieldsets = ((None,{'fields':[
        'appointment',
                'reason',
                'reason_unscheduled',
                'reason_unscheduled_other',
                'info_source',
                'info_source_other',
                'comments'
    ]}),visit_schedule_fieldset_tuple,
        audit_fieldset_tuple)

    radio_fields = {
        'reason': admin.VERTICAL,
        'info_source': admin.VERTICAL}

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)