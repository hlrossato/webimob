# Django settings for webimob project.

import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Higor', 'hl.rossato@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webimob',
        'USER': 'webimob',
        'PASSWORD': 'fkNs8V82b92k',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')
MEDIA_URL = 'http://media.webimob.ambiente-dev.com.br/'

STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')
STATIC_URL = 'http://static.webimob.ambiente-dev.com.br/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'a&q+gwz2c8(974a1xtr=0lyx#(@gzyid0nnka7%oh)h=*hob@a'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'templates')
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'webimob.urls'

WSGI_APPLICATION = 'webimob.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    #third part apps
    'south',
    'gunicorn',
    'tinymce',
    'sorl.thumbnail',
    'localflavor',
    'captcha',

    #apps
    'appsite',
    'banners',
    'empreendimentos',
    'clientes',
    'corretores',
    'imoveis',
    'contato',
)

# E-MAIL =====================================================================
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '4codeweb@gmail.com'
EMAIL_HOST_PASSWORD = 'fourc0d3#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CAPTCHA ======================================================================
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_dots',
)
CAPTCHA_NOISE_COLOR = '#eeeeee'
CAPTCHA_FONT_SIZE = 30

# TINYMCE ======================================================================
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste",
    'paste_text_sticky': True,
    'paste_text_sticky_default': True,
    'theme': "advanced",
    'theme_advanced_buttons1': 
        "bold,italic,underline,strikethrough,|,"+
        "justifyleft,justifycenter,justifyright,justifyfull,|,"+
        "styleselect,formatselect,|,link,unlink,anchor,|,"+
        "table,removeformat,code",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_buttons4': "",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

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

# LOCAL_SETTINGS ===============================================================
try:
    from local_settings import *
except ImportError:
    print 'local_settings.py not found'