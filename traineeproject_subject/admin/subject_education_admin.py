from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import EducationQuestionnaire
from ..forms import EducationQuestionnaireForm
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin
  


@admin.register(EducationQuestionnaire, site=traineeproject_subject_admin)
class EducationQuestionnaireAdmin(SimpleHistoryAdmin):

    form = EducationQuestionnaireForm
    fieldset = (
        (None, {
            'fields': ('employment_status','type_of_work', 'other_work',
             'previous_work_decscription','previous_month_salary'),

        }),
        audit_fieldset_tuple
        )
    list_display = ('employment_status','previous_work_decscription','previous_month_salary')    

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    