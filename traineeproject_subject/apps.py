from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from datetime import datetime
from dateutil.tz import gettz
from edc_visit_tracking.constants import (SCHEDULED, UNSCHEDULED, LOST_VISIT,
                                          MISSED_VISIT, COMPLETED_PROTOCOL_VISIT)
from edc_constants.constants import FAILED_ELIGIBILITY

class AppConfig(DjangoAppConfig):
    app_label = 'traineeproject_subject'
    name = 'traineeproject_subject'
    verbose_name = 'Trainee Subject CRFs'
    admin_site_name = 'traineeproject_subject_admin'
    
    form_versions = {
        'traineeproject_subject.subjectvisit': 1.0,
        'traineeproject_subject.subjectrequisition': 1.0,
        'traineeproject_subject.subjectpersonalcontractinfo': 1.0,
        'traineeproject_subject.subjecteducation': 1.0,
        'traineeproject_subject.subjectdemographic': 1.0,
        'traineeproject_subject.subjectcommunityengagement': 1.0,
        'traineeproject_subject.screeningeligibility': 1.0,
        'traineeproject_subject.consent': 1.0,
    }

if settings.APP_NAME == 'traineeproject_subject':
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.constants import COMPLETE_APPT
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
    from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
    from edc_timepoint.timepoint import Timepoint
    from edc_timepoint.timepoint_collection import TimepointCollection
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU


    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                slots=[100, 100, 100, 100, 100])}
    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'AZD100'
        protocol_number = '150'
        protocol_name = 'Trainee Project'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 4, 1, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
       
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='traineeproject_subject.subjectvisit',
                 appt_type = 'clinic'),
        ]  
        
    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='edc_appointment.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT)
        ])
        
    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        report_datetime_allowance = -1
        visit_models = {
            'traineeproject_subject': ('subject_visit', 'traineeproject_subject.subjectvisit'), }    
        
    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'training_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED, COMPLETED_PROTOCOL_VISIT]
        delete_on_reasons = [LOST_VISIT, MISSED_VISIT, FAILED_ELIGIBILITY]    
        
             


