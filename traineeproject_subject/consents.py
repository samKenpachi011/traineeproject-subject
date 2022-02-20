from datetime import datetime
import arrow
from dateutil.tz import gettz
from django.apps import apps as django_apps

from edc_constants.constants import MALE, FEMALE, OTHER
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents


app_config = django_apps.get_app_config('edc_protocol')
edc_protocol = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v1 = Consent(
    'traineeproject_subject.subjectconsent',
    version='1',
    start=arrow.get(
        datetime(2021, 5, 1, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2022, 5, 31, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=18,
    age_is_adult=18,
    age_max=60,
    gender=[MALE, FEMALE, OTHER])

site_consents.register(v1)