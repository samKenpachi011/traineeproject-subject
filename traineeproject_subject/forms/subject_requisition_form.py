from django import forms
from django import forms
from ..models import SubjectRequisition

class SubjectRequisitionForm(forms.ModelForm):


    class Meta:
        model = SubjectRequisition
        fields = '__all__'