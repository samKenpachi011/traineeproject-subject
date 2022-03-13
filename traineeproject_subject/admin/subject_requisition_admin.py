from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import SubjectRequisition
from ..forms import SubjectRequisitionForm
from edc_model_admin import audit_fieldset_tuple
from .modeladmin_mixins import CrfModelAdminMixin
from edc_lab.admin import (RequisitionAdminMixin,
                           requisition_fieldset,
                           requisition_status_fieldset,
                           requisition_identifier_fieldset,
                           requisition_identifier_fields,
                           requisition_verify_fields,
                           requisition_verify_fieldset)

@admin.register(SubjectRequisition, site=traineeproject_subject_admin)
class SubjectRequisitionAdmin(CrfModelAdminMixin, RequisitionAdminMixin, admin.ModelAdmin):

    form = SubjectRequisitionForm
    ordering = ('requisition_identifier',)
    fieldset = (
        (None,{ 
            'fields': (
                'subject_visit',
                'requisition_datetime',
                'is_drawn',
                'reason_not_drawn',
                'reason_not_drawn_other',
                'drawn_datetime',
                'study_site',
                'panel',
                'item_type',
                'item_type_other',
                'item_count',
                'estimated_volume',
                'priority',
                'urgent_specify',
                'comments',)
                }),
        requisition_fieldset,
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)


    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
    }

    list_display = ('subject_visit', 'is_drawn', 'panel', 'estimated_volume',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj)
                +requisition_identifier_fields
                +requisition_verify_fields)