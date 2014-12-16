from .base  import *

DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'consultorio',
        'USER': 'root',
        'PASSWORD': 'dynamo',
        'HOST' : 'ec2-54-163-255-191.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'
