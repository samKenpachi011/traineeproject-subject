from django import forms
from ..models import SubjectRequisition
from edc_lab.forms.modelform_mixins import RequisitionFormMixin
# from esr21_subject_validation.form_validators import SubjectRequisitionFormValidator
from traineeproject_validation.form_validators import SubjectRequisitionFormValidator


# TODO: Create a subject_validation app to create a SubjectRequisitionFormValidator function 
class FormValidator(forms.ModelForm):

    form_validator_cls = None

    def clean(self):
        cleaned_data = super().clean()
        try:
            form_validator = self.form_validator_cls(
                cleaned_data=cleaned_data,
                instance=self.instance)
        except TypeError:
            pass
        else:
            cleaned_data = form_validator.validate()
        return cleaned_data

class SubjectRequisitionForm(RequisitionFormMixin,FormValidator):
    form_validator_cls = SubjectRequisitionFormValidator

    def clean(self):
        super().clean()
    class Meta:
        model = SubjectRequisition
        fields = '__all__'