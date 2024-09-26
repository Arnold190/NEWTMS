"""
Django settings for PROD project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from Checkpoint.callbacks import permission_callback


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o+@z@(*j0i*pz8ac&0w8(0vg4)@w1-8*l!&^1_k!jpq%$)hjzl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Custom user model
#AUTH_USER_MODEL = 'Checkpoint.CustomUser'

# Application definition

INSTALLED_APPS = [
    
    'frontend', #custom tailwind theme app
    'tailwind',
    'django_extensions',
    #'frontend', #custom tailwind theme app
    
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App',
    'Checkpoint',

    'sass_processor',
    'compressor',
    'widget_tweaks',

    'django.contrib.sites',  # Required by allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

TAILWIND_APP_NAME = 'frontend'
NPM_BIN_PATH = 'F:\\nodejs\\npm.cmd'

# NPM_BIN_PATH = '/f/nodejs/npm'

  #"/path/to/npm"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'PROD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PROD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newtms',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'PASSWORD':'12345',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

#STATIC_URL = 'static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#STATIC_ROOT = BASE_DIR / 'staticfiles'

# Directory where collected static files will be stored
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_STORAGE = 'Checkpoint.storage.CustomStaticStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

BASE_DIR = Path(__file__).resolve().parent.parent


STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

####

STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder', ]

COMPRESS_ENABLED = True

 #COMPRESS

COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Incorrect: Tuple assigned to COMPRESS_ROOT
#COMPRESS_ROOT = (os.path.join(BASE_DIR, 'staticfiles'),)

#COMPRESS_ENABLED = True
#COMPRESS_OFFLINE = True
#COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#COMPRESS_URL = STATIC_URL
#COMPRESS_ROOT = STATIC_ROOT

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = '/static/'


#SASS
SASS_PROCESSOR_ENABLED = True
SASS_PROCESSOR_ROOT = STATICFILES_DIRS[0]  # Adjust as needed




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_ROOT = '/path/to/media/root'
MEDIA_URL = '/media/'


# settings.py
DEFAULT_FILE_STORAGE = 'Checkpoint.storage.CustomStorage'


#Allauth 
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Keep the default authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Add allauth backend
    'Checkpoint.backends.EmailBackend'
    
)

SITE_ID = 1

# Additional settings for allauth
LOGIN_REDIRECT_URL = '/dashboard/'  # Or wherever you want to redirect after login

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
