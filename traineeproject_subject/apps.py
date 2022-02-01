from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from datetime import datetime
from dateutil.tz import gettz
class AppConfig(DjangoAppConfig):
    app_label = 'traineeproject_subject'
    name = 'traineeproject_subject'
    verbose_name = 'Trainee Subject CRFs'
    admin_site_name = 'traineeproject_subject_admin'

if settings.APP_NAME == 'traineeproject_subject':
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'traineeproject_subject':(
                'subject_visit','traineeproject_subject.subjectvisit')}

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP100'
        protocol_number = '100'
        protocol_name = 'Trainee Project'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 4, 1, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='traineeproject_subject.subjectvisit')
        ]       


