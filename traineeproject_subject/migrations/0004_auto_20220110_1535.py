# Generated by Django 3.1.4 on 2022-01-10 15:35

from django.db import migrations, models
import django_crypto_fields.fields.lastname_field
import edc_consent.validators


class Migration(migrations.Migration):

    dependencies = [
        ('traineeproject_subject', '0003_auto_20220110_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectconsent',
            name='consent_to_participate',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='Participant is not eligible if no', max_length=3, validators=[edc_consent.validators.eligible_if_yes], verbose_name='Do you consent to participate in the study?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectconsent',
            name='witness_name',
            field=django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edc_consent.validators.FullNameValidator()], verbose_name="Witness's last and first name"),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='consent_to_participate',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='Participant is not eligible if no', max_length=3, validators=[edc_consent.validators.eligible_if_yes], verbose_name='Do you consent to participate in the study?'),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='witness_name',
            field=django_crypto_fields.fields.lastname_field.LastnameField(blank=True, help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)", max_length=71, null=True, validators=[edc_consent.validators.FullNameValidator()], verbose_name="Witness's last and first name"),
        ),
    ]
