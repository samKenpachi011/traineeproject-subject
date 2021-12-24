from django.apps import AppConfig
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

class TPSConfig(AppConfig):
    app_label = 'traineeproject_subject'
    name = 'traineeproject_subject'
    verbose_name = 'Trainee Subject CRFs'
    admin_site_name = 'traineeproject_subject_admin'
