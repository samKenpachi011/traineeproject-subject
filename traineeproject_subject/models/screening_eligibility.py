from django.db import models
from traineeproject_subject.eligibility import Eligibility
from ..identifiers import ScreeningIdentifier
from .model_mixins import SearchSlugModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugManager
from ..choices import GENDER_OTHER

class ScreeningEligibilityManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)
class ScreeningEligibility(NonUniqueSubjectIdentifierFieldMixin,SiteModelMixin,SearchSlugModelMixin,BaseUuidModel):
    
    identifier_cls = ScreeningIdentifier
    
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    screening_identifier = models.CharField(
        editable=False,
        verbose_name='Screening Eligibility Identifier',
        max_length=36,
        blank=True,
        unique=True,)
        
    age_in_years = models.PositiveIntegerField(
        verbose_name='Age',
        help_text='Age in years.')

    is_guardian_present = models.CharField(
        max_length=5,
        verbose_name='Is guardian available',
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)    

    gender = models.CharField(
        max_length=6,
        verbose_name='Gender',
        help_text='Participant Gender',
        choices=GENDER_OTHER,
        null=True,
        blank=False)

    nationality = models.CharField(
        max_length=3,
        verbose_name='Is the participant a citizen of Botswana',
        default=NOT_APPLICABLE,
        choices=YES_NO_NA
        )

    married_to_citizen = models.CharField(
        max_length=5,
        verbose_name='Is the participant married to a citizen of Botswana',
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    proof_of_marriage = models.CharField(
        max_length=5,
        verbose_name='Has the participant provided proof of marriage',
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)    

    is_literate = models.CharField(
        max_length=3,
        verbose_name='Is the participant literate',
        choices=YES_NO,)

    is_literate_witness_present = models.CharField(
        max_length=5,
        choices=YES_NO,)    

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    reason_for_ineligibility = models.TextField(
        max_length=150,
        verbose_name="Reason for ineligibility",
        null=True,
        editable=False)  
          
    is_consented = models.BooleanField(
        default=False,
        editable=False)

    history = HistoricalRecords()
    
    objects = ScreeningEligibilityManager() 

    def __str__(self):
        return f'{self.screening_identifier}, {self.subject_identifier}'

    def natural_key(self):
        return (self.screening_identifier,)

    natural_key.dependencies = ['sites.Site']

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['screening_identifier',])
        return fields

    def save(self, *args, **kwargs):  
        eligibility_criteria = Eligibility(self.age_in_years)

        self.is_eligible = eligibility_criteria.is_eligible
        self.reason_for_ineligibility = eligibility_criteria.reason_for_ineligibility

        if not self.screening_identifier:
            self.screening_identifier = self.identifier_cls().identifier  
        super().save(*args,**kwargs)

    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Screening Eligibility'
        verbose_name_plural = 'Screening Eligibility'

