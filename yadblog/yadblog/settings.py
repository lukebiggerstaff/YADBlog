import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Environment = {
    "DJANGO_DEBUG" : bool(int(os.environ.get("DJANGO_DEBUG"))),
    "DJANGO_SECRET_KEY": os.environ.get("DJANGO_SECRET_KEY"),
    "DJANGO_DB_NAME": os.environ.get("DJANGO_DB_NAME"),
    "DJANGO_DB_USER": os.environ.get("DJANGO_DB_USER"),
    "DJANGO_DB_PASSWORD": os.environ.get("DJANGO_DB_PASSWORD"),
    "DJANGO_DB_HOST": os.environ.get("DJANGO_DB_HOST"),
    "DJANGO_DB_PORT": os.environ.get("DJANGO_DB_PORT"),
    "DJANGO_SITE_NAME": os.environ.get("DJANGO_SITE_NAME"),
    "DJANGO_EMAIL_BACKEND": os.environ.get("DJANGO_EMAIL_BACKEND"),
    "DJANGO_ADMIN_EMAIL": os.environ.get("DJANGO_ADMIN_EMAIL"),
    "DJANGO_EMAIL_HOST": os.environ.get("DJANGO_ADMIN_EMAIL"),
    "DJANGO_EMAIL_HOST_USER": os.environ.get("DJANGO_ADMIN_EMAIL"),
    "DJANGO_EMAIL_HOST_PASSWORD": os.environ.get("DJANGO_ADMIN_EMAIL"),
}

DEBUG = Environment["DJANGO_DEBUG"]
SECRET_KEY = Environment["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = [Environment['DJANGO_SITE_NAME']]
ADMIN_EMAIL_ADDRESS = Environment["DJANGO_ADMIN_EMAIL"]
EMAIL_HOST = Environment[ "DJANGO_EMAIL_HOST" ]
EMAIL_HOST_USER = Environment[ "DJANGO_EMAIL_HOST_USER" ]
EMAIL_HOST_PASSWORD = Environment[ "DJANGO_EMAIL_HOST_PASSWORD" ]
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': Environment["DJANGO_DB_NAME"],
        'USER': Environment["DJANGO_DB_USER"],
        'PASSWORD': Environment["DJANGO_DB_PASSWORD"],
        'HOST': Environment["DJANGO_DB_HOST"],
        'PORT': Environment["DJANGO_DB_PORT"],
    },
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'blog',
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

ROOT_URLCONF = 'yadblog.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'yadblog.wsgi.application'

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media URL and root
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configure streaming logging
LOGGING = {
    'version': 1,
    'handlers': {
        'console' : {
            'class' : 'logging.StreamHandler',
        },
    },
    'loggers' : {
        'django' : {
            'handlers' : ['console'],
            'level' : os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
