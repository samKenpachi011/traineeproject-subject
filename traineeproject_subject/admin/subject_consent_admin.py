from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import SubjectConsent
from ..forms import SubjectConsentForm

@admin.register(SubjectConsent, site=traineeproject_subject_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    
    form = SubjectConsentForm
    fields = ['gender','report_datetime']