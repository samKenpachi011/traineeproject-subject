from django.test import TestCase
from ..eligibility import Eligibility

class TestScreeningEligibility(TestCase):

    def test_under_age_participant_ineligibility(self):
        """Participant age < 18 are ineligible"""
        eligiblity = Eligibility(age_in_years=16)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Participant is under 18', eligiblity.reason_for_ineligibility)