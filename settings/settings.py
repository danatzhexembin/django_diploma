"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e8t42tj@vnwi&+cd&i5^h0=-@^ywf9(j%*3#nr_7w!lx8r!kle'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

LOGGING_TXT = False

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'daphne',
    'channels',
    'grappelli',
    # 'django.contrib.jinja2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_crontab',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',

    'django_salary',
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

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'django_salary.context_processors.user_access',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'
ASGI_APPLICATION = 'settings.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/db.sqlite3',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'pgs_db',
    #     'USER': 'pgs_usr',
    #     'PASSWORD': '12345Qwerty!',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'special': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_temp',
        'TIMEOUT': '120',
        'OPTIONS': {
            # "MAX_ENTIES": 200,
        }
    },
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [
        Path(BASE_DIR, 'static'),
        # Path(BASE_DIR, 'frontend/public/static'),
        # Path(BASE_DIR, 'frontend/build/static'),
    ]
else:
    STATIC_ROOT = Path(BASE_DIR, 'static')
    STATICFILES_DIRS = [
        # Path(BASE_DIR, 'static_external'),
        # Path(BASE_DIR, 'django_mvt_todo_list/static'),
        # Path(BASE_DIR, 'frontend/build/static'),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

MEDIA_URL = 'media/'
MEDIA_ROOT = Path(BASE_DIR, 'static/media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# drf
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

CRONJOBS = [
    ('0 23 * * *', 'django_salary.cron.my_cron_job'),
]
