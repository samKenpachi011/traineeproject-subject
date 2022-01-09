# Generated by Django 3.1.4 on 2022-01-02 14:15

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityEngagementQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_status', models.CharField(choices=[('very active', 'Very active'), ('somewhat active', 'Somewhat active'), ('not active at all', 'Not active at all'), ('dont_want_to_answer', "Don't want to answer")], default='N/A', help_text='Activities such as burial society, Motshelo, Syndicate,PTA, VDC(Village Development Committee), Mophato and development of the community', max_length=20, verbose_name='How active are you in community activities?')),
                ('previous_election_participation', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('not applicable', 'No elections, cant vote'), ('dont_want_to_answer', "Don't want to answer")], default='N/A', help_text='Previous elections participation', max_length=20, verbose_name='Did you vote in the last local government election?')),
                ('neighbourhood_major_problems', models.CharField(choices=[('hiv and aids', 'HIV/AIDS'), ('schools', 'Schools'), ('sewer', 'Sewer'), ('unemployment', 'Unemployment'), ('roads', 'Roads'), ('water', 'Water'), ('other', 'Other, specify'), ('house', 'House'), ('malaria', 'Malaria')], default='N/A', help_text='Problems in the neighbourhood', max_length=16, verbose_name='What are the major problems in this neighbourhood?')),
                ('adult_participation', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't know"), ('dont_want_to_answer', "Don't want to answer")], default='N/A', help_text='Do the adults work together in solving problems', max_length=20, verbose_name='If there is a problem in this neighborhood, do the adults work together in solving it?')),
                ('report_datetime', models.DateTimeField(help_text='Date and time of report.', verbose_name='Report Date and Time')),
            ],
            options={
                'verbose_name': 'Community Engagement Questionnaire',
                'verbose_name_plural': 'Community Engagement Questionnaire',
            },
        ),
        migrations.CreateModel(
            name='EducationQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6, verbose_name='Are you currently working?')),
                ('type_of_work', models.CharField(choices=[('occasional_or_casual_employment', 'Occasional or casual employment'), ('seasonal_employment', 'Seasonal Employment'), ('formal_wage_employment_full_time', 'Formal wage employment (full-time)'), ('formal_wage_employment_part_time', 'Formal wage employment (part-time)'), ('self_employed_in_agriculture', 'Self employed in agriculture'), ('self_employed_making_money_full_time', 'Self-employed making money (full time)'), ('self_employed_making_money_part_time', 'Self-employed making money (part time)'), ('dont_want_to_answer', "Don't want to answer"), ('OTHER', 'OTHER')], max_length=36, verbose_name='In your main job what type of work do you do?')),
                ('other_work', models.CharField(max_length=100, null=True, verbose_name='What is your other work type?')),
                ('previous_work_decscription', models.CharField(choices=[('farmer', 'Farmer (own land)'), ('farm_worker', 'Farm work on employers land'), ('domestic_worker', 'Domestic worker'), ('bar_hotel_guesthouse_venue_worker', 'Work in bar/ hotel/ guest house/ entertainment venue'), ('entertainer', 'Entertainer'), ('fishing', 'Fishing'), ('mining', 'Mining'), ('tourism_game_parks', 'Tourism / game parks'), ('shop_small_business_worker', 'Working in shop or small business'), ('informal_selling', 'Informal Selling'), ('commercial_sex_work', 'Commercial sex work'), ('truck_taxi_driver', 'Transport (trucker/ taxi driver)'), ('factory_worker', 'Factory worker'), ('guard', 'Guard  (security company)'), ('police_soldier', 'Police/ Soldier'), ('clerical_and_office_work', 'Clerical and office work'), ('government_worker', 'Government worker'), ('teacher', 'Teacher'), ('health_care_worker', 'Health care worker'), ('other_professional', 'Other professional'), ('dont_want_to_answer', "Don't want to answer"), ('OTHER', 'OTHER')], help_text='In the past month, how much money did you earn from workyou did or received in payment?', max_length=36, verbose_name='Describe the work that you do or did in your most recent job.')),
                ('previous_month_salary', models.CharField(choices=[('none', 'NONE'), ('1_199', 'BWP 1 - 199'), ('200_499', 'BWP 200 - 499'), ('500_999', 'BWP 500 - 999'), ('1000_4999', 'BWP 1000 - 4999'), ('5000_10000', 'BWP 5000 - 10000'), ('more_than_10000', 'More than BWP 10000'), ('dont_want_to_answer', "Don't want to answer")], max_length=36, verbose_name='In the past month, how much money did you earn from workyou did or received in payment?')),
            ],
            options={
                'verbose_name': 'Education Questionnaire',
                'verbose_name_plural': 'Education Questionnaire',
            },
        ),
        migrations.CreateModel(
            name='SubjectConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(help_text='Participant Gender', max_length=6, verbose_name='Gender')),
                ('report_datetime', models.DateTimeField(help_text='Date and time of report.', verbose_name='Report Date and Time')),
            ],
            options={
                'verbose_name': 'Subject Consent',
                'verbose_name_plural': 'Subject Consent',
            },
        ),
        migrations.CreateModel(
            name='SubjectRequisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(help_text='Participant Gender', max_length=6, verbose_name='Gender')),
                ('report_datetime', models.DateTimeField(help_text='Date and time of report.', verbose_name='Report Date and Time')),
            ],
            options={
                'verbose_name': 'Subject Requisition',
                'verbose_name_plural': 'Subject Requisition',
            },
        ),
        migrations.CreateModel(
            name='ScreeningEligibility',
            fields=[
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('screening_identifier', models.CharField(blank=True, editable=False, max_length=36, unique=True, verbose_name='Screening Eligibility Identifier')),
                ('age_in_years', models.PositiveIntegerField(help_text='Age in years.', verbose_name='Age')),
                ('is_guardian_present', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Is guardian available')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], help_text='Participant Gender', max_length=6, null=True, verbose_name='Gender')),
                ('nationality', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=3, verbose_name='Is the participant a citizen of Botswana')),
                ('married_to_citizen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Is the participant married to a citizen of Botswana')),
                ('proof_of_marriage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Has the participant provided proof of marriage')),
                ('is_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is the participant literate')),
                ('is_literate_witness_present', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('is_eligible', models.BooleanField(default=False, editable=False)),
                ('reason_for_ineligibility', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason for ineligibility')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Screening Eligibility',
                'verbose_name_plural': 'Screening Eligibility',
            },
        ),
        migrations.CreateModel(
            name='HistoricalScreeningEligibility',
            fields=[
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('screening_identifier', models.CharField(blank=True, db_index=True, editable=False, max_length=36, verbose_name='Screening Eligibility Identifier')),
                ('age_in_years', models.PositiveIntegerField(help_text='Age in years.', verbose_name='Age')),
                ('is_guardian_present', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Is guardian available')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], help_text='Participant Gender', max_length=6, null=True, verbose_name='Gender')),
                ('nationality', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=3, verbose_name='Is the participant a citizen of Botswana')),
                ('married_to_citizen', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Is the participant married to a citizen of Botswana')),
                ('proof_of_marriage', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='Has the participant provided proof of marriage')),
                ('is_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is the participant literate')),
                ('is_literate_witness_present', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('is_eligible', models.BooleanField(default=False, editable=False)),
                ('reason_for_ineligibility', models.TextField(editable=False, max_length=150, null=True, verbose_name='Reason for ineligibility')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Screening Eligibility',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
