from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import CommunityEngagementQuestionnaire
from ..forms import CommunityEngagementQuestionnaireForm
from .modeladmin_mixins import CrfModelAdminMixin

@admin.register(CommunityEngagementQuestionnaire, site=traineeproject_subject_admin)
class CommunityEngagementAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    
    form = CommunityEngagementQuestionnaireForm
    radio_fields = {
        'activity_status': admin.VERTICAL,
        'previous_election_participation': admin.VERTICAL,
        'neighbourhood_major_problems': admin.VERTICAL
    }

