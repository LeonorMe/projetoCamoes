"""
Django settings for projetoCamoes project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
from pathlib import Path
import os
#import environ
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

# Initialise environment variables
#env = environ.Env()
#environ.Env.read_env()
#TODO
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# The root directory of your Django project is the one that contains manage.py

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# Support env variables from .env file if defined
#from dotenv import load_dotenv
#env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
#load_dotenv(env_path)

# TODO
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'we93rni-y23b9jo2pwjinjb_51swn0f.aKOSNED-72uu8568yhevflpwpqmk%&/'
#SECRET_KEY = os.environ["SECRET_KEY"] 
#SECRET_KEY_FALLBACKS = [
#    os.environ["OLD_SECRET_KEY"],
#]

#SECRET_KEY = env('SECRET_KEY')
#SECRET_KEY = os.environ.get('SECRET_KEY')
#SECRET_KEY = os.getenv("SECRET_KEY")

# Deploy
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['camoes500anos.pythonanywhere.com']

CSRF_TRUSTED_ORIGINS = ['https://camoes500anos.pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainPages',
    'authenticationApp',
    'userPages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # language perferences
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# TODO
ROOT_URLCONF = 'projetoCamoes.urls'
#i18n_patterns(*urls, prefix_default_language=True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projetoCamoes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #'NAME': env('DATABASE_NAME'),
        #'USER': env('DATABASE_USER'),
        #'PASSWORD': env('DATABASE_PASS'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "pt"

LANGUAGES = [
    ("en", _("English")),
    ("pt", _("Portuguese")),
] # 'pt-pt' #'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True # Uses internationalization

USE_TZ = True

LOCALE_PATHS = [ 
    os.path.join(BASE_DIR, 'locale/')
]
#"/LEIM2/6sem/Projeto/LEIM-Projeto-Camoes/projetoCamoes/locale",
#os.path.join(BASE_DIR, 'locale/')


''' Logging
import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
'''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
#STATIC_URL = '/...' https://media.example.com/
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#if DEBUG:
#    STATICFILES_DIRS = [
#        BASE_DIR / 'static'
#    ]
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
#else:
    #STATIC_ROOT = BASE_DIR/'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    #STATIC_ROOT = '/LEIM2/6sem/Projeto/LEIM-Projeto-Camoes/projetoCamoes/assets/'


MEDIA_URL = 'media/' #/var/www/example.com/media/  https://media.example.com/
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = BASE_DIR/'media'
#MEDIA_ROOT = '/home/admin/webapps/mainfolder/mainapp/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# redirecionar Login e Logout
#LOGIN_REDIRECT_URL = "mainPages:dashboard_contrib"
#LOGOUT_REDIRECT_URL = "mainPages:login"
