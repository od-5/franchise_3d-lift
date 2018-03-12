import os

from .base import BASE_DIR


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
            # 'loaders': (
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ),
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')
