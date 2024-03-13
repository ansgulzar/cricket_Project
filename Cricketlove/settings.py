"""
Django settings for Cricketlove project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
import dj_database_url
import pyrebase

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\MSI ADMIN\PycharmProjects\pythonProjectcricket\Cricketlove\cricketlive\serviceAccount.json'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ovxz3ht_8yb-&8er^9=^mi_vwlkgz&k6++5+%nz00pl-!-d$^-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cricketlive',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Cricketlove.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'cricketlive/templates')],
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

WSGI_APPLICATION = 'Cricketlove.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Cricketdatabase",
        "USER": "ans.gulzar@auroramy.com",
        "PASSWORD": "Q2NDCS8yZIKa",
        "HOST": "ep-sparkling-moon-a18tnmp5.ap-southeast-1.aws.neon.tech",
        "PORT": "5432",
        'OPTIONS': {'sslmode': 'require'},
    }
}
# DATABASES = {
#     'default': {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "testcricketrender",
#         "USER": "testcricketrender_user",
#         "PASSWORD": "jZddBS3eYqMUm8our8nGXmCITbnEDnIY",
#         "HOST": "dpg-cm57s4ud3nmc73amiuu0-a",
#         "PORT": "5432",
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }
# DATABASE = {
#     "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django_firebase.firebase',
#         'FIREBASE_SERVICE_ACCOUNT_KEYFILE': 'C:/Users/MSI ADMIN/PycharmProjects/pythonProjectcricket/serviceAccount.json',
#     },
# }
# FIREBASE_SERVICE_ACCOUNT_KEYFILE = 'C:/Users/MSI ADMIN/PycharmProjects/pythonProjectcricket/serviceAccount.json'
# FIREBASE_DATABASE_NAME = 'Cricket_test'


# config = {
#     "apiKey": "AIzaSyAUJoJMThd_D4AckGqkYgem9ycXBn5iEjE",
#     "authDomain": "cricket-test-ffaad.firebaseapp.com",
#     "databaseURL": "https://cricket-test-ffaad-default-rtdb.asia-southeast1.firebasedatabase.app",
#     "projectId": "cricket-test-ffaad",
#     "storageBucket": "cricket-test-ffaad.appspot.com",
#     "messagingSenderId": "844917189565",
#     "appId": "1:844917189565:web:d4636a00b50f1f4c4b40d4",
# }
# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_firebase_app.firebase',
#         'CREDENTIALS': config,
#         'NAME': 'default',
#     }
# }

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'cricketlive/static')]
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = '/data/'
