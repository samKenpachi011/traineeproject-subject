from django import forms
from ..models import SubjectDemographicsQuestionnaire
from edc_base.sites import SiteModelFormMixin

class DemographicQuetionnaireForm(SiteModelFormMixin,forms.ModelForm):

    class Meta:
        model: SubjectDemographicsQuestionnaire
        fields = '__all__'