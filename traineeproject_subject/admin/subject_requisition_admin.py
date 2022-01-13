from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import SubjectRequisition
from ..forms import SubjectRequisitionForm
from edc_model_admin import audit_fieldset_tuple
# from .modeladmin_mixins import CrfModelAdminMixin

@admin.register(SubjectRequisition, site=traineeproject_subject_admin)
class SubjectRequisitionAdmin(admin.ModelAdmin):

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
        audit_fieldset_tuple
            )


    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
        'study_site': admin.VERTICAL,
    }

    list_display = ('subject_visit', 'is_drawn', 'panel', 'estimated_volume',)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)