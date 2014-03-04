# django-offline-messages Test Settings

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'offline_messages',
    'tests'
)

ROOT_URLCONF = ''

COVERAGE_ADDITIONAL_MODULES = ('offline_messages',)

SECRET_KEY = 'foobar'
