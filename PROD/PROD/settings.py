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
    'PROD.middleware.AutoLogoutMiddleware',
    'PROD.middleware.ClockInOutMiddleware',
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

WHITENOISE_MANIFEST_STRICT = False

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

####

STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder', 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    
    ]

COMPRESS_ENABLED = True

 #COMPRESS

#COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

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


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "SCOW TMS Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "SCOW ADMIN",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "TMS ADMIN",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": 'images/newlogo.png', #{% static '/images/newlogo.png' %}

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": 'images/newlogo.png',

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "images/newlogo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-square",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "/images/newlogo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Schroeder Co-Worker TMS Admin",

    # Copyright on the footer
    "copyright": "SCHROEDER CO-WORKER IT Dept",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        #{"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
   # "usermenu_links": [
       # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
       # {"model": "auth.user"}
    #],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}


############################

# Sessions and Cookies
AUTO_LOGOUT_DELAY = 120  # In minutes

# Session timeout duration in seconds (e.g., 120 minutes-2Hours)
SESSION_COOKIE_AGE = 120 * 60  # 120 minutes

# Make the session expire after the user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# If you want to refresh the session timeout on each request
SESSION_SAVE_EVERY_REQUEST = True

SESSION_IDLE_TIMEOUT = 120  # Set this to the number of minutes for the idle timeout