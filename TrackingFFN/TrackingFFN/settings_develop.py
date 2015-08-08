from TrackingFFN.settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trackingffn',
        'USER': 'trackingffn',
        'PASSWORD': 'TrackingFFN',
        'HOST': '127.0.0.1',
    }
}

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'