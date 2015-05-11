"""
Django settings for lhpoa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
gettext = lambda s: s


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Set later if not in production, else must be defined in local_settings.py
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.messages',
    'lhpoa',

    'twitter_bootstrap',
    'jquery',
    'compressor',

    # Django CMS
    'djangocms_text_ckeditor',
    'treebeard',
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'sorl.thumbnail',


    # Install plugins as needed
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    'djangocms_snippet',
    'slideshow',
    'adminsortable',

    'reversion',
    'cms_bootstrap_templates',
)

# These got overridden by Django CMS
#MIDDLEWARE_CLASSES = ( ...

ROOT_URLCONF = 'lhpoa.urls'

WSGI_APPLICATION = 'lhpoa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

# Settings for compressor and bootstrap
import twitter_bootstrap
my_app_less = os.path.join(BASE_DIR, 'static', 'less')
bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'twitter_bootstrap', 'less')


COMPRESS_ENABLED = False
COMPRESS_LESSC_COMMAND = 'lessc --include-path={}'.format(os.pathsep.join([bootstrap_less, my_app_less]))
COMPRESS_LESSC_COMMAND += " {infile} {outfile}"

COMPRESS_PRECOMPILERS = (
    ('text/less', COMPRESS_LESSC_COMMAND),
    ('stylesheet/less', COMPRESS_LESSC_COMMAND),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Settings for Django CMS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

SITE_ID = 1

MIGRATION_MODULES = {
    'menus': 'menus.migrations_django',

    # Add also the following modules if you're using these plugins:
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_snippet': 'djangocms_snippet.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}

CMS_TEMPLATES = (
    ('lhpoa/landing.html', 'Landing Page'),
    ('cms_bootstrap_templates/template_one_column.html', 'One columns'),
    ('cms_bootstrap_templates/template_two_column.html', 'Two columns'),
    ('cms_bootstrap_templates/template_three_column.html', 'Three columns'),
    ('cms_bootstrap_templates/template_header_two_column.html', 'Two columns with a header'),
    ('cms_bootstrap_templates/template_header_two_column_left.html', 'Two columns w/ header, large left'),
    ('cms_bootstrap_templates/template_header_two_column_right.html', 'Two columns w/ header, large right'),
)


# Import local settings
try:
    from local_settings import *
except:
    pass

if DEBUG and SECRET_KEY == '':
    SECRET_KEY = '+59$_1gzcxv$fdgtd%dd84)3$vc#bud_)zyn3($0r3!u%k*v8+'
elif DEBUG == False:
    raise "You need to define a secret key!"
