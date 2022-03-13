from django.db import models
from django.apps import apps as django_apps
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from ..choices import (GENDER_OTHER, MARITAL_STATUS,LIVING_WITH,LANGUAGES, 
                       IDENTITY_TYPE,DATE_ESTIMATED, DATE_ESTIMATED_NA)
from .model_mixins import SearchSlugModelMixin
from ..subject_identifier import SubjectIdentifier
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow,age
from edc_base.model_fields import IsDateEstimatedField
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NO
from edc_search.model_mixins import SearchSlugManager
from django_crypto_fields.fields import FirstnameField, LastnameField, EncryptedCharField,IdentityField
# edc consent
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.managers import ConsentManager
from edc_consent.field_mixins import (IdentityFieldsMixin,                                  
                                      PersonalFieldsMixin,VulnerabilityFieldsMixin)
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_consent.validators import eligible_if_yes, FullNameValidator
from edc_consent.field_mixins import (SampleCollectionFieldsMixin,ReviewFieldsMixin,CitizenFieldsMixin)
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_base.model_validators.date import datetime_not_future
from edc_protocol.validators import datetime_not_before_study_start


class SubjectScreeningError(Exception):
    pass

class ConsentManager(SubjectConsentManager, SearchSlugManager):
    def get_by_natural(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)
        
    class Meta:
        abstract = True    
        

class SubjectConsent(
        ConsentModelMixin, SiteModelMixin, SampleCollectionFieldsMixin,
        UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin,
        IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
        CitizenFieldsMixin, SearchSlugModelMixin, BaseUuidModel):

    subject_screening_model = 'traineeproject_subject.screeningeligibility'  


    screening_identifier = models.CharField(
        max_length=50,
        verbose_name='Screening identifier',)

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        default=get_utcnow,
        help_text='Date and time of consent.')  


    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=IDENTITY_TYPE)

    language = models.CharField(
        verbose_name='Language of consent',
        max_length=50,
        choices=settings.LANGUAGES,
        null=True,
        blank=True,
        help_text=(
            'The language used for the consent process will '
            'also be used during data collection.')
    )

    consent_reviewed = models.CharField(
        verbose_name='I have reviewed the consent with the participant',
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, participant is not eligible.')

    study_questions = models.CharField(
        verbose_name=(
            'I have answered all questions the participant had about the study'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, participant is not eligible.')

    assessment_score = models.CharField(
        verbose_name=(
            'I have asked the participant questions about this study and '
            'the participant has demonstrated understanding'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, participant is not eligible.')

    verbal_script = models.CharField(
        verbose_name=('I have documented participant\'s details on the verbal '
                      'script, and signed electronically'),
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=False,
        help_text='If no, participant is not eligible.')


    objects = SubjectConsentManager()

    consent = ConsentManager()
    
    history = HistoricalRecords()    

    def __str__(self):
        return f'{self.subject_identifier}  V{self.version}'

    def natural_key(self):
        return (self.subject_identifier, self.version,)   

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields 

    def save(self, *args, **kwargs):
        self.version = '1' 
        super().save(*args, **kwargs)
    
    def make_new_identifier(self):
        """Returns a new and unique identifier.
        Override this if needed. Can be inherited from NonUniqueSubjectIdentifierModelMixin
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier     


    @property
    def consent_version(self):
        return self.version
    
    class Meta(ConsentModelMixin.Meta):
        app_label = 'traineeproject_subject'
        verbose_name = 'Subject Consent'
        get_latest_by = 'consent_datetime'
        unique_together = (
            ('subject_identifier', 'version'),                       
            ('first_name', 'date_of_birth', 'initials', 'version'))
        ordering = ('-created',)
