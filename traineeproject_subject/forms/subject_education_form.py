from ..models import EducationQuestionnaire
from .form_mixins import SubjectModelFormMixin
class EducationQuestionnaireForm(SubjectModelFormMixin):

    class Meta:
        model = EducationQuestionnaire
        fields = '__all__'