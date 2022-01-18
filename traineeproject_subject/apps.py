from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
class AppConfig(DjangoAppConfig):
    app_label = 'traineeproject_subject'
    name = 'traineeproject_subject'
    verbose_name = 'Trainee Subject CRFs'
    admin_site_name = 'traineeproject_subject_admin'

if settings.APP_NAME == 'traineeproject_subject':
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'traineeproject_subject':(
                'subject_visit','traineeproject_subject.subjectvisit')}




