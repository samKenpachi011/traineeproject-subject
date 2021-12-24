from django import forms
from django import forms
from ..models import EducationQuestionnaire

class EducationQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = EducationQuestionnaire
        fields = '__all__'