from django.db import models

class SubjectRequisition(models.Model):
    gender = models.CharField(
        max_length=6,
        verbose_name='Gender',
        help_text='Participant Gender'
    )

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        help_text='Date and time of report.'
    )
    
    class Meta:
        app_label = 'traineeproject_subject'
        verbose_name = 'Subject Requisition'
        verbose_name_plural = 'Subject Requisition'
