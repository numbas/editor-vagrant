# coding: utf-8
import imp
import os
import sys
from database import DATABASES

SITE_TITLE = 'Numbas'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/srv/numbas/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/srv/numbas/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v+z=e61+%_vqkpyd$#w!csr4q@mz&ag9+p&-&24wee!wwo1=0%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment *one* of the two lines below to enable Shibboleth authentication, then look at shib_auth.py.dist and/or numbas_auth.py.
    #'shibboleth.middleware.ShibbolethRemoteUserMiddleware',
    #'numbas_auth.NumbasShibbolethRemoteUserMiddleware',
)

ROOT_URLCONF = 'numbas.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'sanitizer',
    'accounts',
    'analytical',
    'editor',
    'registration',
    'django_tables2',
    'taggit',
	'reversion',
)

SOUTH_MIGRATION_MODULES = {
	'taggit': 'taggit.south_migrations',
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

GLOBAL_SETTINGS = {
    'NUMBAS_PATH': '/srv/numbas/dist',
    'PREVIEW_PATH': '/srv/numbas/previews',
	'PREVIEW_URL': '/numbas-previews/',    #a URL which serves files from PREVIEW_PATH
    'HELP_URL': 'http://numbas-editor.readthedocs.org',        #the URL of the Numbas webdocs
    'PYTHON_EXEC': '/usr/bin/python3',
    'NUMBAS_THEMES': [('Standard','default'),('Printable worksheet','worksheet')],
    'NUMBAS_LOCALES': [('English','en-GB'),(u'Bokmål','nb-NO'),('Nederlands','nl-NL'),(u'Español','es-ES')],
    #Uncomment the line below and provide a path to a minification tool to minify javascript files
    #'MINIFIER_PATH': 'uglifyjs',
}

ALLOW_REGISTRATION = False
ACCOUNT_ACTIVATION_DAYS = 10

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
CAN_LOGOUT = True
CAN_CHANGE_PASSWORD = True

SESSION_COOKIE_HTTPONLY = True

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "editor.context_processors.global_settings",
)

sys.path.append(os.path.join(GLOBAL_SETTINGS['NUMBAS_PATH'],'bin'))

AUTHENTICATION_BACKENDS = (
    # Uncomment to enable LDAP authentication, then look at ldap_auth.py.dist
    #'django_auth_ldap.backend.LDAPBackend',
    # Uncomment to enable the RemoteUser backend for Shibboleth authentication
    #'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# Settings for sending email. Other backends are available - see https://docs.djangoproject.com/en/dev/topics/email/#obtaining-an-instance-of-an-email-backend
#DEFAULT_FROM_EMAIL = 'numbas@domain'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = ''
#EMAIL_PORT = 25
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = False
#EMAIL_FILE_PATH = '/tmp/email/'

# Uncomment to enable LDAP authentication, then look at ldap_auth.py.dist
#from ldap_auth import *
# Uncomment to enable Shibboleth authentication, then look at shib_auth.py.dist
#from shib_auth import *

SANITIZER_ALLOWED_TAGS = ['a', 'p', 'img','br','strong','em','div','code','i','b', 'ul', 'ol', 'li', 'table','thead','tbody','td','th','tr']
SANITIZER_ALLOWED_ATTRIBUTES = ['href','title']
