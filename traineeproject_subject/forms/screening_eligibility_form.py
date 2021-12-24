from django import forms
from ..models import ScreeningEligibility

# to include formvalidators

class ScreeningEligibilityForm(forms.ModelForm):

    class Meta:
        model: ScreeningEligibility
        fields = '__all__'
        