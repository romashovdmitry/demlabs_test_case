# Python imports
from os import getenv, path
from pathlib import Path
from datetime import timedelta

# one-string default settings
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv("SECRET_KEY", "secretos_007")
ROOT_URLCONF = "main.urls"
WSGI_APPLICATION = "main.wsgi.application"
STATIC_URL = "static/"
STATIC_ROOT = "static"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# if project running on production server
IS_PROD = int(getenv("IS_PROD", "0"))

if IS_PROD:
    ALLOWED_HOSTS = [
        "localhost",
        str(getenv("HOST"))
    ]
    DEBUG = False

# if it's running on local machine
else:
    ALLOWED_HOSTS = ['*']
    DEBUG = True

print(f'ALLOWED SHOT - > {ALLOWED_HOSTS}\nDEBUG -> {DEBUG}')


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # collection of custom extensions for the Django Framework
    # https://django-extensions.readthedocs.io/en/latest/ 
    "django_extensions",
    # basic app
    "main",
    # beatiful admin panel
    "adminlte3",
    # Swagger
    "drf_spectacular",
    "drf_spectacular_sidecar",
    # JWT
    "rest_framework_simplejwt",
    # created apps
    "user"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('POSTGRES_DB'),
        'USER': getenv('POSTGRES_USER'),
        'PASSWORD': getenv('POSTGRES_PASSWORD'),
        'HOST': 'demlabs_database',
        'PORT': getenv('POSTGRES_PORT')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

""" custom (not default) additional settings """

# AUTH_USER_MODEL = 'user.User'
# code bellow doesn't work, resolve straightforward
AUTH_USER_MODEL = "user.User"

MEDIA_URL = getenv("MEDIA_URL", "")
MEDIA_ROOT = path.join(BASE_DIR,getenv("MEDIA_ROOT", ""))

REST_FRAMEWORK = {
    # swagger drf-spectacular
    'DEFAULT_SCHEMA_CLASS': 
        'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERERS': [
        'drf_spectacular.renderers.SpectacularRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
    # JWT
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # auth
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated'
    ),
    # throttling
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day'
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(getenv("ACCESS_TOKEN_LIFETIME"))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(getenv("REFRESH_TOKEN_LIFETIME"))
    ),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": getenv("JWT_SECRET_KEY"),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DEMLABS Test Case',
    'DESCRIPTION': 'DEBLABS MVP Shop',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # https://stackoverflow.com/a/67522312/24040439
    # https://drf-spectacular.readthedocs.io/en/latest/faq.html#filefield-imagefield-is-not-handled-properly-in-the-schema
    "COMPONENT_SPLIT_REQUEST": True
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "user.authentication.CustomAuthenication"
]