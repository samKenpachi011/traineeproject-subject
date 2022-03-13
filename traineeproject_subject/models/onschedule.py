from enum import unique
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager

from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

class OnSchedule(OnScheduleModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    schedule_name = models.CharField(
        max_length=25,
        blank=True,
        null=True)

    objects = SubjectIdentifierManager()

    onsite = CurrentSiteManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta(OnScheduleModelMixin.Meta):
        app_label = 'traineeproject_subject'
        unique_together = ('subject_identifier', 'schedule_name')
