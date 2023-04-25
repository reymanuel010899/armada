"""
Django settings for armada project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n(^uu34=h6@c04459s43)u=5frz5@eg0gop0fi!x9#g4wybw6z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://armada-production.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'home',
    'users',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'armada.urls'

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
                'home.context_processors.amigos_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'armada.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASE_URL = "postgresql://postgres:Sibx1rGNTgfjZBX4yYll@containers-us-west-172.railway.app:5511/railway"
 
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

AUTH_USER_MODEL = 'users.User'
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

TIME_ZONE =  'America/Santo_Domingo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR/ "media"

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
 
# ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER =  'socialkiptly@gmail.com'
EMAIL_HOST_PASSWORD = 'yhjqipyhlnhhiwlj'
EMAIL_USE_TLS = True



# aws s3

AWS_ACCESS_KEY_ID = 'AKIASGUFTBD6YOPLRY5L'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGES_BUCKET_NAME = 'armadard'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'%AWS_STORAGES_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl':'max-age=86400'}
AWSS_DEFAULT_ACL = 'public-read'

AWS_LOCATION = 'STATIC'
STATICFILES_DIRS = [
    BASE_DIR / "static",
 
]

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' %(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR/ "media"

PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'home.storage_backend.MediaStore'