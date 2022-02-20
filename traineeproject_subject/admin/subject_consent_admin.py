from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import SubjectConsent
from ..forms import SubjectConsentForm

@admin.register(SubjectConsent, site=traineeproject_subject_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    
    form = SubjectConsentForm
    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'consent_datetime',
                'first_name',
                'last_name',
                'initials',
                'gender',
                'date_of_birth',
                'is_dob_estimated',
                'identity',
                'confirm_identity',
                'identity_type',
                'marital_status',
                'partner_count',
                'currently_living_with',
                'consent_to_participate',
                'consent_to_optional_sample_collection',

            ),
        }),
    )

    search_fields = ('subject_identifier',)

    radio_fields = {
        'gender': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'identity_type': admin.VERTICAL
    }

    readonly_fields = ('subject_identifier',)