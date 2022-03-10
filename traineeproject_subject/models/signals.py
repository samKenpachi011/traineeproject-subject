import imp
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from edc_base.utils import get_utcnow
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.schedule import Schedule
from .subject_consent import SubjectConsent
from .screening_eligibility import ScreeningEligibility
from .onschedule import OnSchedule

@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if created:
            
            # onschedule_obj = django_apps.get_model('traineeproject_subject.onschedule')  
            update_model_fields(instance=instance,
                                model_cls=ScreeningEligibility,
                                fields=[['subject_identifier',instance.subject_identifier],
                                        ['is_consented', True]])
         
        # put_on_schedule(instance=instance)    
        try:
            OnSchedule.objects.get(
                subject_identifier=instance.subject_identifier, )
        except OnSchedule.DoesNotExist:
            onschedule_model = 'traineeproject_subject.onschedule'
            put_on_schedule(schedule_name='traineeproject_schedule', instance=instance, onschedule_model=onschedule_model)    
            
 
# def put_on_schedule(instance=None):
    
#     if instance:
#         _, schedule = site_visit_schedules.get_by_onschedule_model('traineeproject_subject.onschedule')
        
#         schedule.put_on_schedule(
#             subject_identifier=instance.subject_identifier,
#             onschedule_datetime=instance.consent_datetime)
        
    
#         try:
#             onschedule_obj = OnSchedule.objects.get(
#             subject_identifier=instance.subject_identifier,
#             onschedule_datetime=instance.consent_datetime)
#         except OnSchedule.DoesNotExist: 
#             schedule.put_on_schedule(
#             subject_identifier=instance.subject_identifier,
#             onschedule_datetime=instance.consent_datetime)      
#         else:
#             schedule.refresh_schedule(
#                 subject_identifier=instance.subject_identifier,
#                 onschedule_datetime=instance.consent_datetime) 
#             onschedule_obj.save()
            
            
def put_on_schedule(schedule_name,onschedule_model,instance=None):
    
    if instance:
        _, schedule = site_visit_schedules.get_by_onschedule_model(onschedule_model)
        
        onschedule_model_cls = django_apps.get_model(onschedule_model)       
        try:
            onschedule_model_cls.objects.get(
            subject_identifier=instance.subject_identifier,
            schedule_name=schedule_name)
        except onschedule_model_cls.DoesNotExist: 
            schedule.put_on_schedule(
            subject_identifier=instance.subject_identifier,
            onschedule_datetime=instance.consent_datetime,
            schedule_name=schedule_name)      
        else:
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)
            
def update_model_fields(instance=None, model_cls=None, fields=None):
    try:
        model_obj = model_cls.objects.get(
            screening_identifier=instance.screening_identifier)
    except model_cls.DoesNotExist:
        raise ValidationError(f'{model_cls} object does not exist!')
    else:
        for field, value in fields:
            setattr(model_obj, field, value)
        model_obj.save_base(update_fields=[field[0] for field in fields])            
        