from django import forms
from django import forms
from ..models import CommunityEngagementQuestionnaire

class CommunityEngagementQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = CommunityEngagementQuestionnaire
        fields = '__all__'


