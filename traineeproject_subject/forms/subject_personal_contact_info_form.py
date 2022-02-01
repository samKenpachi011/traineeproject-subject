from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from traineeproject_validation.form_validators import PersonalContactInformationFormValidator

from ..models import PersonalContactInfo


class PersonalContactInfoForm(SiteModelFormMixin,FormValidatorMixin,forms.ModelForm):
    
    form_validator_cls = PersonalContactInformationFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    
    class Meta:
        model=PersonalContactInfo
        fields='__all__'