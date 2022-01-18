from django.utils.translation import ugettext_lazy as _
from .constants import DWTA
from edc_constants.constants import OTHER, MALE, FEMALE, NONE,NOT_APPLICABLE
from edc_visit_tracking.constants import MISSED_VISIT, COMPLETED_PROTOCOL_VISIT
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from edc_lab.choices import TUBE

GENDER_OTHER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other')),
)

#Community Questionnaire Choices
ACTIVITY_STATUS = [
    ('very active','Very active'),
    ('somewhat active','Somewhat active'),
    ('not active at all','Not active at all'),
    ('dont_want_to_answer',"Don't want to answer")
]

ELECTION_PARTICIPATION = [
    ('yes','Yes'),
    ('no','No'),
    ('not applicable','No elections, cant vote'),
    ('dont_want_to_answer',"Don't want to answer"),
]

NEIGHBOURHOOD_PROBLEMS = [
    ('hiv and aids',"HIV/AIDS"),
    ('schools','Schools'),
    ('sewer','Sewer'),
    ('unemployment','Unemployment'),
    ('roads','Roads'),
    ('water','Water'),
    ('other',"Other, specify"),
    ('house','House'),
    ('malaria','Malaria'),
]

ADULT_PARTICIPATION = [
    ('yes','Yes'),
    ('no','No'),
    ('dont_know',"Don't know"),
    ('dont_want_to_answer',"Don't want to answer"),
]

# Education Questionnaire

TYPE_OF_WORK = [
    ('occasional_or_casual_employment', 'Occasional or casual employment'),
    ('seasonal_employment', 'Seasonal Employment'),
    ('formal_wage_employment_full_time', 'Formal wage employment (full-time)'),
    ('formal_wage_employment_part_time', 'Formal wage employment (part-time)'),
    ('self_employed_in_agriculture', 'Self employed in agriculture'),
    ('self_employed_making_money_full_time', 'Self-employed making money (full time)'),
    ('self_employed_making_money_part_time', 'Self-employed making money (part time)'),
    ('dont_want_to_answer', DWTA),
    (OTHER, _('Other'))
]

PREVIOUS_JOB_DESCRIPTION = [
    ('farmer', 'Farmer (own land)'),
    ('farm_worker', 'Farm work on employers land'),
    ('domestic_worker', 'Domestic worker'),
    ('bar_hotel_guesthouse_venue_worker', 'Work in bar/ hotel/ guest house/ entertainment venue'),
    ('entertainer', 'Entertainer'),
    ('fishing', 'Fishing'),
    ('mining', 'Mining'),
    ('tourism_game_parks', 'Tourism / game parks'),
    ('shop_small_business_worker', 'Working in shop or small business'),
    ('informal_selling', 'Informal Selling'),
    ('commercial_sex_work', 'Commercial sex work'),
    ('truck_taxi_driver', 'Transport (trucker/ taxi driver)'),
    ('factory_worker', 'Factory worker'),
    ('guard', 'Guard  (security company)'),
    ('police_soldier', 'Police/ Soldier'),
    ('clerical_and_office_work', 'Clerical and office work'),
    ('government_worker', 'Government worker'),
    ('teacher', 'Teacher'),
    ('health_care_worker', 'Health care worker'),
    ('other_professional', 'Other professional'),
    ('dont_want_to_answer', DWTA),
    (OTHER, OTHER)
]

PREVIOUS_MONTH_SALARY = [
    (NONE, NONE.upper()),
    ('1_199', 'BWP 1 - 199'),
    ('200_499', 'BWP 200 - 499'),
    ('500_999', 'BWP 500 - 999'),
    ('1000_4999', 'BWP 1000 - 4999'),
    ('5000_10000', 'BWP 5000 - 10000'),
    ('more_than_10000', 'More than BWP 10000'),
    ('dont_want_to_answer', DWTA),
]

# Consent
MARITAL_STATUS = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed')
]

LIVING_WITH = [
    ('alone', 'Alone'),
    ('partner_or_spouse', 'Partner or spouse'),
    ('siblings', 'Siblings'),
    ('other', 'Other'),
    ('dont_want_to_answer', DWTA)
]

LANGUAGES = [
    ('setswana','Setswana'),
    ('english','English'),
]

IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('passport', 'Passport'),
    ('birth_certificate', 'Birth Certificate'),
    (OTHER, _('Other')),
)

DATE_ESTIMATED = (
    ('-', 'No'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)
DATE_ESTIMATED_NA = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('not_estimated', 'No.'),
    ('D', 'Yes, estimated the Day'),
    ('MD', 'Yes, estimated Month and Day'),
    ('YMD', 'Yes, estimated Year, Month and Day'),
)

# Subject Visit
VISIT_INFO_SOURCE = (
    ('clinic_visit_w_subject', 'Clinic visit with participant'),
    ('other_contact_w_subject',
     'Other contact with participant (i.e telephone call)'),
    ('contact_w_health_worker', 'Contact with health care worker'),
    ('Contact_w_family_design',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other,specify'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Did not attend scheduled visit'),
    (UNSCHEDULED, 'Unscheduled visit/contact'),
    (LOST_VISIT, 'Use only when withdrawing subject off study'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study'),
)

# Requisition

HUBS = (
    ('greater_francistown', 'Greater Francistown'),
    ('greater_gaborone', 'Greater Gaborone'),
    ('ngami', 'Ngami'),
    ('greater_selibe_phikwe', 'Greater Selibe Phikwe'),
    ('serowe_or_palapye', 'Serowe/Palapye')
)

ITEM_TYPE = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TUBE, 'Tube'),
    ('swab', 'Swab'),
    (OTHER, 'Other'),
)

PRIORITY = (
    ('normal', 'Normal'),
    ('urgent', 'Urgent'),
)

REASON_NOT_DRAWN = (
    ('not_collected', 'Not collected'),
    ('not_required', 'Not required at this visit'),
    ('measurement_skipped', 'Measurement skipped at this visit'),
    ('subject_refused', 'Subject refused'),
    ('equipment_malfunction', 'Equipment malfunction'),
    ('staff_unavailable', 'Staff unavailable'),
    ('no_further_information', 'No further information'),
    (OTHER, 'Other, specify'),
    (NOT_APPLICABLE, 'Not applicable'),
)

# Demographic Data
ETHNICITY = (
    ('Black African', 'Black African'),
    ('Caucasian', 'Caucasian'),
    ('Asian', 'Asian'),
    (OTHER, 'Other, specify'),)

HIGHEST_EDUCATION = (
    ('None', 'None'),
    ('Primary', 'Primary'),
    ('Junior Secondary', 'Junior Secondary'),
    ('Senior Secondary', 'Senior Secondary'),
    ('Tertiary', 'Tertiary'),)

SETTLEMENT_TYPE = (
    ('urban', 'Urban'),
    ('rural', 'Rural'),
)        

EMPLOYMENT_STATUS = (
    ('formal-wage_employment_part_time', 'Formal wage employment (Part-time)'),
    ('formal_wage_employment-full_time)',
     'Formal wage employment (full-time)'),
    ('self_employed_full_time)', 'Self-employed (full time)'),
    ('self_employed_part_time)', 'Self-employed (part time)'),
    ('adhoc_work', 'Ad-hoc work'),
    ('Seasonal_employment', 'Seasonal employment'),
    (OTHER, 'Other (specify)'),)