from django.contrib import admin
from ..admin_site import traineeproject_subject_admin
from ..models import CommunityEngagementQuestionnaire
from ..forms import CommunityEngagementQuestionnaireForm

@admin.register(CommunityEngagementQuestionnaire, site=traineeproject_subject_admin)
class CommunityEngagementAdmin(admin.ModelAdmin):
    
    form = CommunityEngagementQuestionnaireForm
    fields = ['gender','report_datetime']