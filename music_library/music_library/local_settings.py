try:
    from music_library.local_settings import *
except ImportError:
    pass

SECRET_KEY = 'django-insecure-+1=)k2#-vps-s61fs3u27e3s@d@ev-2b7wxqhrtkf!f3pzwpdl'

# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Milestine3306',
        'Host': '127.0.01',
        'PORT': '3306',
        'OPTIONS':{
            'autocommit': True
        }
    }
}