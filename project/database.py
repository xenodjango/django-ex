import os

from django.conf import settings


engines = {
    #'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    #'mysql': 'django.db.backends.mysql',
}


def config():
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')
    #if service_name:
        #engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
    #else:
        #engine = engines['sqlite']
    #name = os.getenv('DATABASE_NAME')
    name="default"
    #if not name and engine == engines['sqlite']:
        #name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    engine = engines['postgresql']
    print('DATABASE_USER:', os.getenv('DATABASE_USER'))
    print('DATABASE_PASSWORD:', os.getenv('DATABASE_PASSWORD'))
    print('DJANGO_SECRET_KEY:', os.getenv('DJANGO_SECRET_KEY'))
    return {
        'ENGINE':'django.db.backends.postgresql_psycopg2',#engine,
        'NAME': 'default',#name,
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': '172.30.58.116', #os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'PORT': '5432',#os.getenv('{}_SERVICE_PORT'.format(service_name)),
    }
