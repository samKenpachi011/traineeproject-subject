import arrow

from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.modelform_mixins import VisitTrackingModelFormMixin

from ..models import SubjectVisit

class SubjectModelFormMixin(SiteModelFormMixin, VisitTrackingModelFormMixin,
                            FormValidatorMixin, forms.ModelForm):

    visit_model = SubjectVisit