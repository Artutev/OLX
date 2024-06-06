"""
Django settings for django_settings project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wgy9njj#a8!&qdka+x!l8xqx3vpr9%9bbrm=$^_lfk)9_e_b)("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "daphne",
    "channels",
    #
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_app",
]

"""MIDDLEWARE - промежуточный слой, в виде ООП.
Выполняется в КАЖДОМ запросе.

Тут помещают только обработчики request. Возможно логи.
"""
MIDDLEWARE = [
    "django_app.middleware.CustomCorsMiddleware",  # CUSTOM
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # пробрасывает ошибки в HTMl
                "django.template.context_processors.request",  # пробрасывает данные в HTMl
                "django.contrib.auth.context_processors.auth",  # пробрасывает авторизацию в HTMl
                "django.contrib.messages.context_processors.messages",  # пробрасывает всплывающие сообщения
                "django_app.context_processors.get_user_count",  # CUSTOM
            ],
        },
    },
]

WSGI_APPLICATION = "django_settings.wsgi.application"
ASGI_APPLICATION = "django_settings.asgi.application"

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "django_usr",
        "PASSWORD": "Qwerty!1234$",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    },
    # psycopg2 - win, psycopg2-binary - lin
    # создать пользователя (postgres - DANGER)
    # создать базу с правами на этого пользователя
    #
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    "special": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
        "TIMEOUT": "120",
        "OPTIONS": {
            # "MAX_ENTIES": 200,
        },
    },
    # 'extra': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': env("REDIS_LOCATION")',
    #     'TIMEOUT': '240',
    #     'OPTIONS': {
    #         # "MAX_ENTIES": 200,
    #         "PASSWORD": "12345qwertY!"
    #     }
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Etc/GMT-6"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

"""
Django в режиме DEBUG сам "обслуживает" статику - сам её выдаёт браузеру.
В режиме PRODUCTION - статику "браузеру" будет отдавать Nginx.
"""

STATIC_URL = "/static/"
STATIC_ROOT = Path(BASE_DIR / "staticroot")  # центральная папка для сбора статики
STATICFILES_DIRS = [  # массив, с папками, откуда Django "собирает" статику
    Path(BASE_DIR / "static"),
    # Path(BASE_DIR / "react/build/static"),
    # Path(BASE_DIR / "static")
]

# TODO UPLOAD
MEDIA_URL = "/media/"  # /static/media/
MEDIA_ROOT = Path(BASE_DIR / "static/media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"