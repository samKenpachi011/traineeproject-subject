from django.db import models
from ..choices import ACTIVITY_STATUS, ELECTION_PARTICIPATION, NEIGHBOURHOOD_PROBLEMS,ADULT_PARTICIPATION
from edc_constants.constants import NOT_APPLICABLE
from edc_search.model_mixins import SearchSlugManager
from .model_mixins import CrfModelMixin

class CommunityEngagementQuestionnaireManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)
class CommunityEngagementQuestionnaire(CrfModelMixin):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        help_text='Date and time of report.')

    activity_status = models.CharField(
        max_length=20,
        verbose_name='How active are you in community activities?',
        help_text='Activities such as burial society, Motshelo, Syndicate,'
        'PTA, VDC(Village Development Committee), Mophato and development of the community',
        choices=ACTIVITY_STATUS,
        default=NOT_APPLICABLE)

    previous_election_participation = models.CharField(
        max_length=20,
        verbose_name='Did you vote in the last local government election?',
        help_text='Previous elections participation',
        choices=ELECTION_PARTICIPATION,
        default=NOT_APPLICABLE)    

    neighbourhood_major_problems  = models.CharField(
        max_length=16,
        verbose_name='What are the major problems in this neighbourhood?',
        help_text='Problems in the neighbourhood',
        choices=NEIGHBOURHOOD_PROBLEMS,
        default=NOT_APPLICABLE)
    
    adult_participation = models.CharField(
        max_length=20,
        verbose_name='If there is a problem in this neighborhood, do the adults work together in solving it?',
        help_text='Do the adults work together in solving problems',
        choices=ADULT_PARTICIPATION,
        default=NOT_APPLICABLE)

    
    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Community Engagement Questionnaire'
        verbose_name_plural = 'Community Engagement Questionnaire'
