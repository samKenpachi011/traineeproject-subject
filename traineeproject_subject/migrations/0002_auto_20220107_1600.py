# Generated by Django 3.1.4 on 2022-01-07 16:00

import django.core.validators
from django.db import migrations, models
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import edc_base.model_fields.date_estimated
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('traineeproject_subject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectconsent',
            name='report_datetime',
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='confirm_identity',
            field=django_crypto_fields.fields.identity_field.IdentityField(help_text='Retype the identity number (Encryption: RSA local)', max_length=71, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='consent_datetime',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of consent.', verbose_name='Consent date and time'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='consent_to_optional_sample_collection',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, verbose_name='Do you consent to optional sample collection?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='consent_to_participate',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='Participant is not eligible if no', max_length=3, verbose_name='Do you consent to participate in the study?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='currently_living_with',
            field=models.CharField(choices=[('alone', 'Alone'), ('partner_or_spouse', 'Partner or spouse'), ('siblings', 'Siblings'), ('other', 'Other'), ('dont_want_to_answer', "Don't want to answer")], default='---------', max_length=20),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='first_name',
            field=django_crypto_fields.fields.firstname_field.FirstnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='identity',
            field=django_crypto_fields.fields.identity_field.IdentityField(default=1234567, help_text=' (Encryption: RSA local)', max_length=71, verbose_name='Identity number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='identity_type',
            field=models.CharField(choices=[('country_id', 'Country ID number'), ('passport', 'Passport'), ('birth_certificate', 'Birth Certificate'), ('OTHER', 'Other')], default='---------', max_length=20, verbose_name='What type of identity number is this?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='initials',
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[django.core.validators.RegexValidator(message='Ensure initials consist of letters only in upper case, no spaces.', regex='^[A-Z]{2,3}$')]),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='is_dob_estimated',
            field=edc_base.model_fields.date_estimated.IsDateEstimatedField(choices=[('-', 'No'), ('D', 'Yes, estimated the Day'), ('MD', 'Yes, estimated Month and Day'), ('YMD', 'Yes, estimated Year, Month and Day')], help_text='If the exact date is not known, please indicate which part of the date is estimated.', max_length=25, null=True, verbose_name='Is date of birth estimated?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='is_literate',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text="If 'No' provide witness's name on this form and signature on the paper document.", max_length=3, verbose_name='Is the participant literate?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='language',
            field=models.CharField(blank=True, choices=[('setswana', 'Setswana'), ('english', 'English')], help_text='The language used for the consent process will also be used during data collection.', max_length=50, null=True, verbose_name='Language of consent'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='last_name',
            field=django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], default='---------', max_length=8, verbose_name='What is your marital status?'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='other_gender',
            field=models.CharField(max_length=100, null=True, verbose_name='If other specify...'),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='partner_count',
            field=models.PositiveIntegerField(default=1, verbose_name='Who do you currently live with?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='screening_identifier',
            field=models.CharField(default=None, max_length=50, verbose_name='Screening identifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='witness_name',
            field=django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, verbose_name="Witness's last and first name"),
        ),
        migrations.AlterField(
            model_name='educationquestionnaire',
            name='type_of_work',
            field=models.CharField(choices=[('occasional_or_casual_employment', 'Occasional or casual employment'), ('seasonal_employment', 'Seasonal Employment'), ('formal_wage_employment_full_time', 'Formal wage employment (full-time)'), ('formal_wage_employment_part_time', 'Formal wage employment (part-time)'), ('self_employed_in_agriculture', 'Self employed in agriculture'), ('self_employed_making_money_full_time', 'Self-employed making money (full time)'), ('self_employed_making_money_part_time', 'Self-employed making money (part time)'), ('dont_want_to_answer', "Don't want to answer"), ('OTHER', 'Other')], max_length=36, verbose_name='In your main job what type of work do you do?'),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], help_text='Participant Gender', max_length=6, null=True, verbose_name='Gender'),
        ),
    ]
