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

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = ''

COVERAGE_ADDITIONAL_MODULES = ('offline_messages',)

SECRET_KEY = 'foobar'
