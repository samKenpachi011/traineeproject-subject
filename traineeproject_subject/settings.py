#from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#zf+(wfwer6t$(d&8@u2urv6_8jv1u*vvruveoysrku9tdo$cg'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#APP_LABEL = 'traineeproject_subject'
APP_NAME = 'traineeproject_subject'
SITE_ID = 1
DEVICE_ID =99
REVIEWER_SITE_ID = 1
# ETC
ETC_DIR= '/etc/'

# KEY PATH
# KEY_PATH = os.path.join(ETC_DIR, APP_NAME, 'crypto_fields')

# Application definition

AUTO_CREATE_KEYS=False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'django_crypto_fields.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_identifier.apps.AppConfig', 
    'edc_locator.apps.AppConfig',
    'edc_base.apps.AppConfig', 
    'edc_device.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_metadata.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'traineeproject_validation.apps.AppConfig',
    'traineeproject_subject.apps.EdcAppointmentAppConfig',
    'traineeproject_subject.apps.EdcProtocolAppConfig',
    'traineeproject_subject.apps.EdcVisitTrackingAppConfig',
    'traineeproject_subject.apps.EdcMetadataAppConfig',
    'traineeproject_subject.apps.EdcTimepointAppConfig',
    'traineeproject_subject.apps.AppConfig',
    'traineeproject_prn.apps.AppConfig',
    'traineeproject_visit_schedule.apps.AppConfig',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'traineeproject_subject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'traineeproject_subject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# dashboards
DASHBOARD_URL_NAMES = {
    'screening_listboard_url': 'traineeproject_dashboard:screening_listboard_url',
    'subject_listboard_url': 'traineeproject_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'traineeproject_dashboard:subject_dashboard_url',
    
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DASHBOARD_URL_NAMES = {}
