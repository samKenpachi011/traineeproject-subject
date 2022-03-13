from django import forms
from ..models import SubjectRequisition

from .form_mixins import SubjectModelFormMixin
from edc_metadata.constants import NOT_REQUIRED


class SubjectRequisitionForm(SubjectModelFormMixin):
    # requisition_identifier = forms.CharField(
    #     label='Requisition identifier',
    #     widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        clean_data = super().clean()
        if clean_data.get('reason_not_drawn') == NOT_REQUIRED:

            super().clean()

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
