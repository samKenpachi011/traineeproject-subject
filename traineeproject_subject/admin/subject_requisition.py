from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import SubjectRequisition
from ..forms import SubjectRequisitionForm

@admin.register(SubjectRequisition, site=traineeproject_subject_admin)
class SubjectRequisitionAdmin(admin.ModelAdmin):

    form = SubjectRequisitionForm
    fields = ['gender','report_datetime']