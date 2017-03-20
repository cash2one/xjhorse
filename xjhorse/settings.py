"""
Django settings for xjhorse project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_d*=$^f+c2)t@_7h9f4p(u%ijkq@_2aqy=8w=8+&8zkxy&ld-%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.xjhorse.net']

# Application definition
AUTHENTICATION_BACKENDS = (

    # 尽管有了allauth，Django admin仍然需要以下认证模块来完成通过用户名登录
    'django.contrib.auth.backends.ModelBackend',

    # allauth特定的认证方法，如通过e-mail登录
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 便于使用bootstrap forms
    'bootstrap3',

    #  allauth在django需要以下配置
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.baidu',     # 百度
    'allauth.socialaccount.providers.douban',    # 豆瓣
    'allauth.socialaccount.providers.weixin',    # 微信
    'allauth.socialaccount.providers.facebook',  # 脸谱
    'allauth.socialaccount.providers.google',    # 谷歌
    'allauth.socialaccount.providers.github',    # github


     # 新疆马业首页
    'homePage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xjhorse.urls'

# allauth在django需要以下配置
SITE_ID = 1
# 登录成功后重定向URL
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],  #, 'publish_stream'],
        'METHOD': 'oauth2'  # 'js_sdk'  # instead of 'oauth2'
    },
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },
}


CRISPY_TEMPLATE_PACK = "bootstrap3"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth'), ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # needed for admin templates
                'django.contrib.auth.context_processors.auth',
                # these *may* not be needed
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # allauth needs this from django
                'django.template.context_processors.request',
            ],
        }
    },
]

WSGI_APPLICATION = 'xjhorse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

LANGUAGES = (
  ('en-us', 'English'),
  ('zh-cn', 'Chinese'),
)

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# 告诉Django除了在每个app中寻找静态文件之外，还可以在项目根目录的static目录中寻找静态文件
# 独立于具体app的共用静态文件夹，位于项目根目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 当运行python manage.py collectstatic时，Django会把所有静态文件收集到项目根目录的staticfiles目录中
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
