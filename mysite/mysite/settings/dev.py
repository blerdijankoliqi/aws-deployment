from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q+n0v_-uncu&17h28_d3%cbal35dbfn%mn&fl%&rmiq_jebgza'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', '52.57.207.200'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
