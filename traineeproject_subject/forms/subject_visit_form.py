from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from ..models import SubjectVisit
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.form_validators import VisitFormValidator 
class SubjectVisitForm (
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
