from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from edc_action_item.site_action_items import site_action_items
from edc_base.utils import get_utcnow

@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    pass          