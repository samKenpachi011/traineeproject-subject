from django.db import models


class ScreeningEligibility(models.Model):

    age_in_years = models.CharField(
        max_length=5,
        verbose_name='Age',
        help_text='Age in years.'
    )

    gender = models.CharField(
        max_length=6,
        verbose_name='Gender',
        help_text='Participant Gender'
    )

    nationality = models.CharField(
        max_length=36,
        verbose_name='Nationality',
        help_text='Date and time of report.'  
    )

    is_literate = models.CharField(
        max_length=5,
        verbose_name='Report Date and Time',
        help_text='Date and time of report.'
    )

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        help_text='Date and time of report.'
    )

    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Screening Eligibility'
        verbose_name_plural = 'Screening Eligibility'

