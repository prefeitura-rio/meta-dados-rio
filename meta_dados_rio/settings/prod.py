# -*- coding: utf-8 -*-
from os import getenv

from meta_dados_rio.settings.base import *

DEBUG = False
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    }
}

ADMINS = [("Gabriel Milan", "gabriel.gazola@poli.ufrj.br")]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = getenv("EMAIL_HOST_USER")
SERVER_EMAIL = getenv("EMAIL_HOST_USER")
