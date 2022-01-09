from django import forms
from ..models import ScreeningEligibility
from edc_base.sites import SiteModelFormMixin

# to include formvalidators

class ScreeningEligibilityForm(SiteModelFormMixin,forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model: ScreeningEligibility
        fields = '__all__'
        