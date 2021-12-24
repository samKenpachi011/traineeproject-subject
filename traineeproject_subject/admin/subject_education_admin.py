from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import EducationQuestionnaire
from ..forms import EducationQuestionnaireForm

@admin.register(EducationQuestionnaire, site=traineeproject_subject_admin)
class EducationQuestionnaireAdmin(admin.ModelAdmin):

    form = EducationQuestionnaireForm
    fields = ['gender','report_datetime']