from django.db import models
from django.apps import apps as django_apps
from django.core.validators import MinValueValidator
from django.db import models
from .model_mixins import SearchSlugModelMixin
from django.utils import timezone
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin,PreviousVisitModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from django.db.models.deletion import PROTECT
from edc_base.model_validators.date import datetime_not_future
from edc_lab.models import RequisitionModelMixin
from edc_lab.models import RequisitionStatusMixin,RequisitionIdentifierMixin
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_reference.model_mixins import RequisitionReferenceModelMixin
from edc_constants.constants import NOT_APPLICABLE
from ..choices import HUBS, ITEM_TYPE, PRIORITY,REASON_NOT_DRAWN

from .subject_visit import SubjectVisit
from edc_search.model_mixins import SearchSlugManager

class SubjectRequisitionManager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass
class SubjectRequisition(
    NonUniqueSubjectIdentifierFieldMixin,
    RequisitionModelMixin,RequisitionStatusMixin,RequisitionIdentifierMixin,
    VisitTrackingCrfModelMixin,SubjectScheduleCrfModelMixin,
    PreviousVisitModelMixin,RequiresConsentFieldsModelMixin,
    RequisitionReferenceModelMixin,UpdatesRequisitionMetadataModelMixin,
    SearchSlugModelMixin,BaseUuidModel):

    lab_profile_name = 'traineeproject_subject'

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    requisition_datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='Requisition Date and Time',
        validators=[datetime_not_future, ])

    reason_not_drawn = models.CharField(
        verbose_name='If not drawn, please explain',
        max_length=25,
        default=NOT_APPLICABLE,
        choices=REASON_NOT_DRAWN)

    drawn_datetime = models.DateTimeField(
        verbose_name='Date / Time Specimen Drawn',
        validators=[datetime_not_future, ],
        null=True,
        blank=True,
        help_text=(
            'If not drawn, leave blank.'))    

    study_site = models.CharField(
        verbose_name='Study site',
        choices=HUBS,
        max_length=25, )   

    item_type = models.CharField(
        verbose_name='Item collection type',
        max_length=25,
        choices=ITEM_TYPE,
        default=NOT_APPLICABLE)    

    item_count = models.PositiveIntegerField(
        verbose_name='Total number of items',
        help_text=(
            'Number of tubes, samples, etc being sent for this test/order only. '
            'Determines number of labels to print'),
        null=True,
        blank=True)  

    estimated_volume = models.DecimalField(
        verbose_name='Estimated volume in mL',
        validators=[
            MinValueValidator(0, message="Cannot be a negative number"),
        ],
        max_digits=7,
        decimal_places=2,
        help_text=(
            'If applicable, estimated volume of sample for this test/order. '
            'This is the total volume if number of "tubes" above is greater than 1'),
        null=True,
        blank=True) 

    priority = models.CharField(
        verbose_name='Priority',
        max_length=25,
        choices=PRIORITY,
        default='normal', )   

    urgent_specify = models.TextField(
        verbose_name='If urgent, please specify',
        max_length=250,
        null=True,
        blank=True, )

    comments = models.TextField(
        max_length=350,
        null=True,
        blank=True)  
    
    object = SubjectRequisitionManager()
    
    history = HistoricalRecords()    

    def __str__(self):
        return (
            f'{self.requisition_identifier} '
            f'{self.panel_object.verbose_name}')       
        
    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.protocol_number = edc_protocol_app_config.protocol_number
        self.report_datetime = self.requisition_datetime
        self.subject_identifier = self.subject_visit.subject_identifier
        # self.consent_model = 'traineeproject_subject.subject_consent'
        super().save(*args, **kwargs)
           
           
    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend([
            'requisition_identifier',
            'human_readable_identifier', 'identifier_prefix'])
        return fields        
    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Subject Requisition'
        unique_together = ('panel', 'subject_visit')
