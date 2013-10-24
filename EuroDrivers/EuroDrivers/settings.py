# Django settings for EuroDrivers project.

DEBUG = True        # FIXME 
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Michał Pilch', 'mpilhoo@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'eurodrivers',
        'USER': 'ueurodrivers',                      # Not used with sqlite3.
        'PASSWORD': 'driversue',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/London'

SITE_ID = 1

LANGUAGE_CODE = 'en-GB'
USE_I18N = True
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '50%8zf275o%yd#x(kfz4@djon=54ora77ji=!5$widv61_#iau'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_auth.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'EuroDrivers.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'EuroDrivers.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    #'social_auth',
    'Website'
)

#AUTHENTICATION_BACKENDS = (
    #'social_auth.backends.twitter.TwitterBackend',
    #'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    #'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #'social_auth.backends.OpenIDBackend',
    #'django.contrib.auth.backends.ModelBackend',
#)

## TODO
#TWITTER_CONSUMER_KEY         = ''
#TWITTER_CONSUMER_SECRET      = ''
#FACEBOOK_APP_ID              = ''
#FACEBOOK_API_SECRET          = ''
#GOOGLE_CONSUMER_KEY          = ''
#GOOGLE_CONSUMER_SECRET       = ''
#GOOGLE_OAUTH2_CLIENT_ID      = ''
#GOOGLE_OAUTH2_CLIENT_SECRET  = ''
#YAHOO_CONSUMER_KEY           = ''
#YAHOO_CONSUMER_SECRET        = ''

#LOGIN_URL          = '/login-form/'
#LOGIN_REDIRECT_URL = '/logged-in/'
#LOGIN_ERROR_URL    = '/login-error/'

#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

#SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
#SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True   # TODO verify
#SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
#SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]
#SOCIAL_AUTH_SESSION_EXPIRATION = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
