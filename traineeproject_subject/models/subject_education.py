from django.db import models
from edc_constants.choices import YES_NO

from edc_constants.constants import NOT_APPLICABLE, NO
from ..choices import TYPE_OF_WORK,PREVIOUS_JOB_DESCRIPTION,PREVIOUS_MONTH_SALARY
from edc_base.model_managers import HistoricalRecords
from edc_search.model_mixins import SearchSlugManager
from .subject_visit import SubjectVisit
from .model_mixins import CrfModelMixin

class EducationQuestionnaireManager(SearchSlugManager, models.Manager):
    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)
    

class EducationQuestionnaire(CrfModelMixin):
    
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.PROTECT)

    employment_status = models.CharField(
        max_length=6,
        verbose_name='Are you currently working?',
        choices=YES_NO,
        default=NO,)

    type_of_work = models.CharField(
        max_length=36,
        verbose_name='In your main job what type of work do you do?',
        choices=TYPE_OF_WORK)

    other_work = models.CharField(
        max_length=100,
        verbose_name='What is your other work type?',
        null=True)

    previous_work_decscription = models.CharField(
        max_length=36,
        verbose_name='Describe the work that you do or did in your most recent job.',
        help_text='In the past month, how much money did you earn from work'
                     'you did or received in payment?',
        choices=PREVIOUS_JOB_DESCRIPTION)

    previous_month_salary = models.CharField(
        max_length=36,
        verbose_name='In the past month, how much money did you earn from work'
                     'you did or received in payment?',
        choices=PREVIOUS_MONTH_SALARY)
  
    history = HistoricalRecords()    
    
    def __str__(self):
        return f'{self.subject_identifier}'

    def natural_key(self):
        return self.subject_identifier

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Education Questionnaire'
        verbose_name_plural = 'Education Questionnaire'
