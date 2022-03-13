from django.db import models
from django.apps import apps as django_apps
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
from edc_constants.choices import YES_NO
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
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager


class SubjectScreeningError(Exception):
    pass

class ConsentManager(SubjectConsentManager, SearchSlugManager):
    def get_by_natural(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)
        
    class Meta:
        abstract = True    
        

class SubjectConsent(
        ConsentModelMixin, SiteModelMixin,
        UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
        PersonalFieldsMixin, VulnerabilityFieldsMixin,
        SearchSlugModelMixin, BaseUuidModel):

    subject_screening_model = 'traineeproject_subject.screeningeligibility'    

    screening_identifier = models.CharField(
        max_length=50,
        verbose_name='Screening identifier',)

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        default=get_utcnow,
        help_text='Date and time of consent.')  

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))],
        null=True, blank=False)   


    language = models.CharField(
        max_length=50,
        verbose_name='Language of consent',
        choices=LANGUAGES,
        null=True,
        blank=True,
        help_text=(
            'The language used for the consent process will '
            'also be used during data collection.')) 

    is_literate = models.CharField(
        max_length=3,
        verbose_name='Is the participant literate?',
        choices=YES_NO,
        help_text=('If \'No\' provide witness\'s name on this '
                   'form and signature on the paper document.'),
        default=NO,)

    witness_name = LastnameField(
        verbose_name='Witness\'s last and first name',
        validators=[FullNameValidator()],
        blank=True,
        null=True,
        help_text=mark_safe(
            'Required only if participant is illiterate.<br>'
            'Format is \'LASTNAME, FIRSTNAME\'. '
            'All uppercase separated by a comma.'),
    )        

    gender = models.CharField(
        max_length=6,
        verbose_name='Gender',
        help_text='Participant Gender',
        choices=GENDER_OTHER,
        null=True,
        blank=False)

    other_gender = models.CharField(
        max_length=100,
        verbose_name='If other specify...',
        null=True)    
    
    date_of_birth = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False)

    is_dob_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?",
        null=True,
        blank=False)

    marital_status = models.CharField(
        max_length=8,
        choices=MARITAL_STATUS,
        verbose_name='What is your marital status?',
        default='---------',
        )  

    partner_count = models.PositiveIntegerField(
        verbose_name='Number of Partners?',
        null=True
        )

    currently_living_with = models.CharField(
        max_length=20,
        verbose_name='Who do you currently live with?',
        choices=LIVING_WITH,
        default='---------')

    identity = IdentityField(
        verbose_name='Identity number')

    identity_type = models.CharField(
        max_length=20,
        verbose_name='What type of identity number is this?',
        choices=IDENTITY_TYPE,
        default='---------',) 

    confirm_identity = IdentityField(
        help_text='Retype the identity number',
        null=True,
        blank=False)    

    consent_to_participate = models.CharField(
        max_length=3,
        verbose_name='Do you consent to participate in the study?',
        choices=YES_NO,    
        validators=[eligible_if_yes, ],
        help_text='Participant is not eligible if no',
        default=NO)    

    consent_to_optional_sample_collection = models.CharField(
        max_length=3,
        verbose_name='Do you consent to optional sample collection?',
        choices=YES_NO,
        default=NO) 


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
