from faker import Faker
from models import SubjectConsent
from model_mommy.recipe import Recipe, seq
from edc_base.utils import get_utcnow
from dateutil.relativedelta import relativedelta
from edc_constants.constants import YES, NO


fake = Faker()

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    consent_datetime=get_utcnow(),
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials='XX',
    gender='F',
    language='en',
    identity_type='OMANG',
    is_dob_estimated=NO,
    citizen=YES,
    version='1',
)