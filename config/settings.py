import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'test-secret-key-12345')
DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['django.contrib.contenttypes']
ROOT_URLCONF = 'config.urls'
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']