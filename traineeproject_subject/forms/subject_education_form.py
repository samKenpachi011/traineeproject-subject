from django import forms
from django import forms
from ..models import EducationQuestionnaire
from edc_base.sites import SiteModelFormMixin

class EducationQuestionnaireForm(SiteModelFormMixin,forms.ModelForm):

    class Meta:
        model = EducationQuestionnaire
        fields = '__all__'