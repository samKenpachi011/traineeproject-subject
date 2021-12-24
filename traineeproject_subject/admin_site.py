from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'TraineeProject Subject'
    site_title = 'TraineeProject Subject'
    index_title = 'TraineeProject Subject'

traineeproject_subject_admin = AdminSite(name='traineeproject_subject_admin')
