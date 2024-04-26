"""
Django settings for soft project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! #这里改了下次的jwt就会失效，请注意！！
SECRET_KEY = 'django-insecure-(5r0)!@)-4mt@s1enh0fond$eq$+%-z*m&s2k(hpr*(d(%jf8)'
MySOLT = "AJDADKLASNLKZHFOIAEJFQAWFKOWFNZSJMP[OC"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    "daphne.apps.DaphneConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "channels",
    "rest_framework",
    "tranapp.apps.TranappConfig",
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "tools.core.CorsMiddleWare",
]

ROOT_URLCONF = 'soft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'soft.wsgi.application'
ASGI_APPLICATION = 'soft.asgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
# 设置上传文件的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 指定根目录加载文件的路径

ADMIN_SITE_HEADER = '二手书交易小程序后台管理'
ADMIN_SITE_TITLE = '二手书交易小程序后台管理'
# 日志相关配置
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     # 日志的格式
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
#         },
#     },
#     # 日志的过滤信息
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # 日志的处理方式配置
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             # 日志位置,日志文件名,日志保存目录必须手动创建
#             'filename': os.path.join(os.path.dirname(BASE_DIR), "soft/logs/test.log"),
#             # 日志文件的最大值,这里我们设置300M
#             'maxBytes': 300 * 1024 * 1024,
#             # 日志文件的数量,设置最大日志数量为10
#             'backupCount': 10,
#             # 日志格式:详细格式
#             'formatter': 'verbose'
#         },
#     },
#     # 日志对象
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'propagate': True, # 是否让日志信息继续冒泡给其他的日志处理系统
#         },
#     }
# }

### drf配置

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': "tranapp.utils.exc_.MyExcHandler",  # 异常处理函数
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",

}
