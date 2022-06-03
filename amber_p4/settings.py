"""
Django settings for amber_p4 project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

if os.path.isfile('env.py'):
    import env  # noqa
# noqa means 'no quality assurance' - the linter will not try to validate this line

"""
If there's an environment variable called DEVELOPMENT in the environment,
this variable will be set to its value. 
Otherwise, it'll be false.
"""
development = os.environ.get("DEVELOPMENT", False)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
HIPPO_TEMPLATES = os.path.join(BASE_DIR, "hippotherapy/templates/hippo")
ADMIN_TEMPLATES = os.path.join(BASE_DIR, "administration/templates/admin")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
Using a blank string as the default
will prevent the Django server from even starting 
if this environment variable is not set.
"""
SECRET_KEY = os.environ.get("SECRET_KEY", '')


# SECURITY WARNING: don't run with debug turned on in production!
"""
In dev DEBUG will be true
On Heroku DEBUG will be false
If there's an error on Heroku - we won't expose any internal source code on the error page.
"""
DEBUG = development

"""
This list allows Django to ensure that HTTP requests are coming from domain names it trusts.
Without it malicious users would potentially be able to load malicious scripts,
Poison the cached versions of our pages, 
or even change the reset links in our password reset emails.
By default, Django will block a request from any host not in this list.
"""
if development:
    ALLOWED_HOSTS = ["127.0.0.1"]
else:
    ALLOWED_HOSTS = [os.environ.get("HEROKU_HOSTNAME")]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administration',
    'hippotherapy',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amber_p4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [HIPPO_TEMPLATES, ADMIN_TEMPLATES],
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

WSGI_APPLICATION = 'amber_p4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
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

LANGUAGE_CODE = 'en-ie'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
"""
We will not use STATIC_ROOT on this project.
But it is good practise to set it anyway.  Especially since the website will not work without it!?!
"""
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django messages
MESSAGE_TAGS = {
        messages.DEBUG: 'msg-secondary',
        messages.INFO: 'msg-info',
        messages.SUCCESS: 'ui-state-highlight',
        messages.WARNING: 'msg-warning',
        messages.ERROR: 'ui-state-error',
}

# https://stackoverflow.com/questions/4876370/django-date-format-dd-mm-yyyy
USE_L10N = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d/%m/%y', '%dd/%mm/%Y', '%dd/%mm/%yyyy')

# https://docs.djangoproject.com/en/4.0/topics/i18n/formatting/
# https://stackoverflow.com/questions/4876370/django-date-format-dd-mm-yyyy
FORMAT_MODULE_PATH = [
    'amber.formats',
]

