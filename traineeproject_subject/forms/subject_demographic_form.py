from ..models import SubjectDemographicsQuestionnaire
from .form_mixins import SubjectModelFormMixin

class DemographicQuetionnaireForm(SubjectModelFormMixin):

    class Meta:
        model: SubjectDemographicsQuestionnaire
        fields = '__all__'