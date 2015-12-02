from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if ON_HEROKU == '1':
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar',
)


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FORCE_HTTP_URL = True
AWS_QUERYSTRING_AUTH = False
AWS_SECRET_ACCESS_KEY = os.environ.get('AWSSecretKey')
AWS_ACCESS_KEY_ID = os.environ.get('AWSAccessKeyId')

AWS_STORAGE_BUCKET_NAME = 'om-swig'

