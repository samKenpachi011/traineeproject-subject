from django.contrib import admin

from ..forms import ScreeningEligibilityForm
from ..models import ScreeningEligibility
from ..admin_site import traineeproject_subject_admin


@admin.register(ScreeningEligibility, site=traineeproject_subject_admin)
class ScreeningEligibilityAdmin(admin.ModelAdmin):

    form = ScreeningEligibilityForm
    fields = ['age_in_years', 'gender', 'nationality']

  
