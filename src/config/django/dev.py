from .base import *  # noqa

DEBUG = env.bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

DOMAIN = env.str("DOMAIN", default="")
DATABASE_URL = env.db("DATABASE_URL", default="")

if DATABASE_URL:
    DATABASES = {"default": DATABASE_URL}
