# Generated by Django 3.1.4 on 2022-01-10 10:52

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import django_revision.revision_field
import edc_base.model_fields.custom_fields
import edc_base.model_fields.date_estimated
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.sites.managers
import edc_base.utils
import edc_protocol.validators
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('edc_appointment', '0016_auto_20220110_1052'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('traineeproject_subject', '0002_auto_20220107_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectconsent',
            options={'get_latest_by': 'consent_datetime', 'ordering': ('-created',), 'verbose_name': 'Subject Consent', 'verbose_name_plural': 'Subject Consent'},
        ),
        migrations.AlterModelManagers(
            name='subjectconsent',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='comment',
            field=django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='consent_identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='A unique identifier for this consent instance'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='created',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='device_created',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='device_modified',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='dm_comment',
            field=models.CharField(editable=False, help_text='see also edc.data manager.', max_length=150, null=True, verbose_name='Data Management comment'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='hostname_created',
            field=models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='hostname_modified',
            field=edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='is_verified',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='is_verified_datetime',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='modified',
            field=models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='report_datetime',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='revision',
            field=django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='sid',
            field=models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='site',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='slug',
            field=models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='subject_identifier',
            field=models.CharField(default=None, max_length=50, verbose_name='Subject Identifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='subject_identifier_aka',
            field=models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='subject_identifier_as_pk',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='updates_versions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='user_created',
            field=edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='user_modified',
            field=edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='verified_by',
            field=models.CharField(editable=False, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='version',
            field=models.CharField(default=1, editable=False, help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='id',
            field=edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='subjectconsent',
            unique_together={('first_name', 'date_of_birth', 'initials', 'version'), ('subject_identifier', 'version')},
        ),
        migrations.CreateModel(
            name='HistoricalSubjectVisit',
            fields=[
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
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of this report', validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Visit Date and Time')),
                ('reason_unscheduled_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for unscheduled visit, specify')),
                ('reason_missed_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for missed visit, specify')),
                ('study_status', models.CharField(max_length=50, null=True, verbose_name="What is the participant's current study status")),
                ('require_crfs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10, verbose_name='Are scheduled data being submitted with this visit?')),
                ('info_source_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If "Other" source of information, specify')),
                ('survival_status', models.CharField(choices=[('alive', 'Alive'), ('dead', 'Deceased'), ('unknown', 'Unknown')], default='alive', max_length=10, null=True, verbose_name="Participant's survival status")),
                ('last_alive_date', models.DateField(blank=True, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date participant last known alive')),
                ('comments', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment if any additional pertinent information about the participant')),
                ('reason', models.CharField(choices=[('scheduled', 'Scheduled visit/contact'), ('missed', 'Did not attend scheduled visit'), ('unscheduled', 'Unscheduled visit/contact'), ('lost', 'Use only when withdrawing subject off study'), ('completed protocol', 'Subject has completed the study')], max_length=25, verbose_name='What is the reason for this visit report?')),
                ('reason_missed', models.CharField(blank=True, max_length=250, null=True, verbose_name="If 'Did not attend scheduled visit' is detailed above, reason visit was not attended.")),
                ('reason_unscheduled', models.CharField(blank=True, max_length=25, null=True, verbose_name="If 'Unscheduled' above, provide reason for the unscheduled visit")),
                ('info_source', models.CharField(choices=[('clinic_visit_w_subject', 'Clinic visit with participant'), ('other_contact_w_subject', 'Other contact with participant (i.e telephone call)'), ('contact_w_health_worker', 'Contact with health care worker'), ('Contact_w_family_design', 'Contact with family or designated person who can provide information'), ('OTHER', 'Other,specify')], max_length=40, verbose_name='What is the main source of this information?')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('appointment', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_appointment.appointment')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Visit',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubjectConsent',
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
                ('subject_identifier_as_pk', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('subject_identifier_aka', models.CharField(editable=False, help_text='track a previously allocated identifier.', max_length=50, null=True, verbose_name='Subject Identifier a.k.a')),
                ('is_verified', models.BooleanField(default=False, editable=False)),
                ('is_verified_datetime', models.DateTimeField(editable=False, null=True)),
                ('verified_by', models.CharField(editable=False, max_length=25, null=True)),
                ('report_datetime', models.DateTimeField(editable=False, null=True)),
                ('version', models.CharField(editable=False, help_text="See 'Consent Type' for consent versions by period.", max_length=10, verbose_name='Consent version')),
                ('updates_versions', models.BooleanField(default=False)),
                ('sid', models.CharField(blank=True, editable=False, help_text='Used for randomization against a prepared rando-list.', max_length=15, null=True, verbose_name='SID')),
                ('comment', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Comment')),
                ('dm_comment', models.CharField(editable=False, help_text='see also edc.data manager.', max_length=150, null=True, verbose_name='Data Management comment')),
                ('consent_identifier', models.UUIDField(default=uuid.uuid4, editable=False, help_text='A unique identifier for this consent instance')),
                ('screening_identifier', models.CharField(max_length=50, verbose_name='Screening identifier')),
                ('first_name', django_crypto_fields.fields.firstname_field.FirstnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True)),
                ('last_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Last name')),
                ('consent_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of consent.', verbose_name='Consent date and time')),
                ('initials', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure initials consist of letters only in upper case, no spaces.', regex='^[A-Z]{2,3}$')])),
                ('language', models.CharField(blank=True, choices=[('setswana', 'Setswana'), ('english', 'English')], help_text='The language used for the consent process will also be used during data collection.', max_length=50, null=True, verbose_name='Language of consent')),
                ('is_literate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text="If 'No' provide witness's name on this form and signature on the paper document.", max_length=3, verbose_name='Is the participant literate?')),
                ('witness_name', django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, verbose_name="Witness's last and first name")),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], help_text='Participant Gender', max_length=6, null=True, verbose_name='Gender')),
                ('other_gender', models.CharField(max_length=100, null=True, verbose_name='If other specify...')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of birth')),
                ('is_dob_estimated', edc_base.model_fields.date_estimated.IsDateEstimatedField(choices=[('-', 'No'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, null=True, verbose_name='Is date of birth estimated?')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], default='---------', max_length=8, verbose_name='What is your marital status?')),
                ('partner_count', models.PositiveIntegerField(verbose_name='Who do you currently live with?')),
                ('currently_living_with', models.CharField(choices=[('alone', 'Alone'), ('partner_or_spouse', 'Partner or spouse'), ('siblings', 'Siblings'), ('other', 'Other'), ('dont_want_to_answer', "Don't want to answer")], default='---------', max_length=20)),
                ('identity', django_crypto_fields.fields.identity_field.IdentityField(help_text=' (Encryption: RSA local)', max_length=71, verbose_name='Identity number')),
                ('identity_type', models.CharField(choices=[('country_id', 'Country ID number'), ('passport', 'Passport'), ('birth_certificate', 'Birth Certificate'), ('OTHER', 'Other')], default='---------', max_length=20, verbose_name='What type of identity number is this?')),
                ('confirm_identity', django_crypto_fields.fields.identity_field.IdentityField(help_text='Retype the identity number (Encryption: RSA local)', max_length=71, null=True)),
                ('consent_to_participate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='Participant is not eligible if no', max_length=3, verbose_name='Do you consent to participate in the study?')),
                ('consent_to_optional_sample_collection', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, verbose_name='Do you consent to optional sample collection?')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Consent',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SubjectVisit',
            fields=[
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
                ('consent_model', models.CharField(editable=False, max_length=50, null=True)),
                ('consent_version', models.CharField(editable=False, max_length=10, null=True)),
                ('visit_schedule_name', models.CharField(editable=False, help_text='the name of the visit schedule used to find the "schedule"', max_length=25)),
                ('schedule_name', models.CharField(editable=False, max_length=25)),
                ('visit_code', models.CharField(editable=False, max_length=25, null=True)),
                ('visit_code_sequence', models.IntegerField(blank=True, default=0, help_text='An integer to represent the sequence of additional appointments relative to the base appointment, 0, needed to complete data collection for the timepoint. (NNNN.0)', null=True, verbose_name='Sequence')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of this report', validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Visit Date and Time')),
                ('reason_unscheduled_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for unscheduled visit, specify')),
                ('reason_missed_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=25, null=True, verbose_name='If "Other" reason for missed visit, specify')),
                ('study_status', models.CharField(max_length=50, null=True, verbose_name="What is the participant's current study status")),
                ('require_crfs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10, verbose_name='Are scheduled data being submitted with this visit?')),
                ('info_source_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If "Other" source of information, specify')),
                ('survival_status', models.CharField(choices=[('alive', 'Alive'), ('dead', 'Deceased'), ('unknown', 'Unknown')], default='alive', max_length=10, null=True, verbose_name="Participant's survival status")),
                ('last_alive_date', models.DateField(blank=True, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date participant last known alive')),
                ('comments', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment if any additional pertinent information about the participant')),
                ('reason', models.CharField(choices=[('scheduled', 'Scheduled visit/contact'), ('missed', 'Did not attend scheduled visit'), ('unscheduled', 'Unscheduled visit/contact'), ('lost', 'Use only when withdrawing subject off study'), ('completed protocol', 'Subject has completed the study')], max_length=25, verbose_name='What is the reason for this visit report?')),
                ('reason_missed', models.CharField(blank=True, max_length=250, null=True, verbose_name="If 'Did not attend scheduled visit' is detailed above, reason visit was not attended.")),
                ('reason_unscheduled', models.CharField(blank=True, max_length=25, null=True, verbose_name="If 'Unscheduled' above, provide reason for the unscheduled visit")),
                ('info_source', models.CharField(choices=[('clinic_visit_w_subject', 'Clinic visit with participant'), ('other_contact_w_subject', 'Other contact with participant (i.e telephone call)'), ('contact_w_health_worker', 'Contact with health care worker'), ('Contact_w_family_design', 'Contact with family or designated person who can provide information'), ('OTHER', 'Other,specify')], max_length=40, verbose_name='What is the main source of this information?')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='edc_appointment.appointment')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Visit',
                'ordering': ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'visit_code_sequence', 'report_datetime'),
                'abstract': False,
                'unique_together': {('subject_identifier', 'visit_schedule_name', 'schedule_name', 'visit_code', 'visit_code_sequence'), ('subject_identifier', 'visit_schedule_name', 'schedule_name', 'report_datetime')},
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
