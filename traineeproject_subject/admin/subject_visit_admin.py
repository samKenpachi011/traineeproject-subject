from django.contrib import admin
from django.contrib.admin.sites import site
from ..admin_site import traineeproject_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectVisit

from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_model_admin import audit_fieldset_tuple
from .modeladmin_mixins import ModelAdminMixin

@admin.register(SubjectVisit, site=traineeproject_subject_admin)
class SubjectVisitAdmin(
        VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):
    
    form = SubjectVisitForm
    
    fieldsets = (
        (None,{
            'fields':[
                'appointment',
                'reason',
                'reason_unscheduled',
                'reason_unscheduled_other',
                'info_source',
                'info_source_other',
                'comments'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple)

    radio_fields = {
        'reason': admin.VERTICAL,
        'info_source': admin.VERTICAL}
    
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['timepoint'] = self.get_timepoint(request)

        return super().add_view(
            request, form_url=form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = extra_context or {}

        extra_context['timepoint'] = self.get_timepoint(request)

        return super().change_view(
            request, object_id, form_url=form_url, extra_context=extra_context)