from .base  import *

DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5tn8valh32ctg',
        'USER': 'aqmmhbacbbpxxw',
        'PASSWORD': 'A8rimTOao7gndx_lYClMXIPfbC',
        'HOST' : 'ec2-54-163-255-191.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'
