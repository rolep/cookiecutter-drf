import environ

from configurations import Configuration


class BaseConfiguration(Configuration):
    # Path configurations
    # /config/settings/base.py - 3 = /
    ROOT_DIR = environ.Path(__file__) - 3
    APPS_DIR = ROOT_DIR.path('api')

    # Environment
    env = environ.Env()

    # Apps
    LOCAL_APPS = [
        'api.users',
        'api.utils',
        'api.v1',
    ]
    THIRD_PARTY_APPS = [
        'rest_framework',
        'rest_framework.authtoken',
        'django_filters',
        'rest_auth',
        'rest_auth.registration',
        'allauth',
        'allauth.account',
        'oauth2_provider',
        'corsheaders',
    ]
    DJANGO_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
    ]

    # https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS

    # https://docs.djangoproject.com/en/dev/ref/settings/#middleware
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = env('DJANGO_SECRET_KEY')

    # GENERAL
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = env.bool('DJANGO_DEBUG', False)

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
    APPEND_SLASH = True

    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

    # CORS: https://github.com/ottoyiu/django-cors-headers
    CORS_ORIGIN_WHITELIST = env.tuple(
        'DJANGO_CORS_ORIGIN_WHITELIST',
        default=()
    )

    # https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = 'config.urls'

    # https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'config.wsgi.application'

    # DATABASES
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        # Raises ImproperlyConfigured exception if DATABASE_URL not in
        # os.environ
        'default': env.db(
            default='postgres://postgres:@postgres:5432/postgres',
        ),
    }

    # Static
    # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = str(ROOT_DIR('staticfiles'))

    # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = [
        str(APPS_DIR.path('static')),
    ]

    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    # Templates
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
                ],
            },
        },
    ]

    # Authentication
    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    # django-oauth-toolkit
    OAUTH2_PROVIDER = {
        'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',  # noqa
    }

    # django-allauth
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = 'email'

    # Custom user
    AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # noqa
        'PAGE_SIZE': int(
            env(
                'DJANGO_PAGINATION_LIMIT',
                default=10,
            )
        ),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        )
    }