from edc_action_item import site_action_items
from edc_locator.action_items import SubjectLocatorAction

CONTACT_INFORMATION_ACTION = 'submit-personal-contact-information'


class PersonalContactInformationAction(SubjectLocatorAction):
    name = CONTACT_INFORMATION_ACTION
    display_name = 'Submit Personal Contact Information'
    reference_model = 'traineeproject_subject.personalcontactinfo'
    admin_site_name = 'traineeproject_subject_admin'


site_action_items.register(PersonalContactInformationAction)