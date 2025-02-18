"""
Django settings for D14 project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ei^l(nbk!4!irvc#kz*q^vu4eg*tsps*pd#!ti_i=cifhy9yyk'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# TODO
ALLOWED_HOSTS = []

# Application definition

# TODO
INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_apscheduler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'APPS.lang',
]

# TODO
SITE_ID = 1

# TODO
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'APPS.lang.time.TimezoneMiddleware'

]

ROOT_URLCONF = 'D14.urls'

########################################################################################################################

# TEMPLATE SETTINGS

# TODO
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'TEMPLATES')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

########################################################################################################################

# TODO
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'D14.wsgi.application'

########################################################################################################################

# DATABASE SETTINGS

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# TODO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

########################################################################################################################

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

TIME_ZONE = 'UTC'

########################################################################################################################

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# LANGUAGE SETTINGS

USE_I18N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

########################################################################################################################

USE_TZ = True

########################################################################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# FOR BOOTSTRAP

STATIC_URL = '/STATIC/'

# TODO
STATICFILES_DIRS = [BASE_DIR / "STATIC"]

########################################################################################################################

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

########################################################################################################################

# REDIS SETTINGS

# TODO
# CELERY_BROKER_URL = f'redis://default:2HAqxmH1hHuoPZckq35klXdOaWOtTn1U' \
#                     f'@redis-00000.c16.us-east-1-2.ec2.cloud.redislabs.com:00000'
# CELERY_RESULT_BACKEND = f'redis://default:2HAqxmH1hHuoPZckq35klXdOaWOtTn1U' \
#                         f'@redis-00000.c16.us-east-1-2.ec2.cloud.redislabs.com:00000'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

########################################################################################################################

# CACHE SETTINGS

# TODO
# CACHES = {
#     'default': {
#         'TIMEOUT': 60,
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'CACHE_FILES'),
#     }
# }

########################################################################################################################

# EMAIL SETTINGS

# TODO
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
# LOGIN_REDIRECT_URL = "/"
# ACCOUNT_FORMS = {"signup": "FUNC.forms.CustomSignupForm"}

########################################################################################################################

# ISSUES NOTIFICATION

# TODO
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple_0': {
            "format": "[{asctime}], [{levelname}], [{message}]",
            "style": "{",
        },
        'simple_1': {
            "format": "[{asctime}], [{levelname}], [{module}], [{message}]",
            "style": "{",
        },
        'simple_2': {
            "format": "[{asctime}], [{levelname}], [{message}], [{pathname}]",
            "style": "{",
        },
        'simple_3': {
            "format": "[{asctime}], [{levelname}], [{message}], [{pathname}], [{exc_info}]",
            "style": "{",
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console_I': {  # WORKING ONLY ON DEBUG = False
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'simple_1',
            'filters': ['require_debug_false'],
        },
        'console_D': {  # WORKING ONLY ON DEBUG = True
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_0',
            'filters': ['require_debug_true'],
        },
        'console_W': {  # WORKING ONLY ON DEBUG = True
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_2',
            'filters': ['require_debug_true'],
        },
        'console_E_C': {  # WORKING ONLY ON DEBUG = True
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple_3',
            'filters': ['require_debug_true'],
        },
        'console_E_C_TO_F': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'simple_3'
        },
        'security': {
            # 'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'simple_1'
        },
        'mail_001': {  # WORKING ONLY ON DEBUG = False
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple_2',
            'filters': ['require_debug_false'],
            # "include_html": True  # If you need html problem type
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console_I', 'console_D', 'console_W', 'console_E_C'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console_E_C_TO_F', 'mail_001'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['console_E_C_TO_F', 'mail_001'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console_E_C_TO_F'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console_E_C_TO_F'],
            'propagate': True,
        },
    }
}

########################################################################################################################

# SMTP SETTINGS

# TODO
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # FOR TESTING #
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # FOR REAL TESTING #
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "test@mail.ru"
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "test@mail.ru"

########################################################################################################################

# SEND TO (SETTINGS)

# TODO
EMAIL_SUBJECT_PREFIX = "ISSUES NOTIFICATION"
SERVER_EMAIL = "test@mail.ru"
ADMINS = (
    ('Type name here!', 'test@mail.com'),
)

########################################################################################################################
