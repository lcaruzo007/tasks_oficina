# settings.py
#AQUI NAS PRIMEIRAS LINHAS VAMOS IMPORTAR A BIBLIOTECA OS
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-20_1%(bd8!khad_s1p$baqf+eihn2jn&+n@r)s#ktwj#mko_lv'
 # Adicione uma chave secreta forte aqui

DEBUG = True  # Configure como False em produção

ALLOWED_HOSTS = ['*']  # Defina os hosts permitidos para produção

# Configurações do banco de dados MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tasks_oficina',  # Nome do seu banco de dados
        'USER': 'Caruzo',  # Usuário do banco de dados
        'PASSWORD': '123456',  # Senha do banco de dados
        'HOST': 'localhost',  # Host do banco de dados (pode ser 'localhost')
        'PORT': '3306',  # Porta padrão do MySQL
    }
}

STATIC_URL = '/static/'

# Adicione o diretório 'static' dentro da sua aplicação 'app'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'static'),
]


# Configurações de arquivos de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'app/templates'),
        ],
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

# Configuração do fuso horário
TIME_ZONE = 'America/Sao_Paulo'  # Altere para o fuso horário desejado

# Idioma usado para as mensagens do Django
LANGUAGE_CODE = 'pt-br'

# URLs permitidas para o host
ALLOWED_HOSTS = ['*']

# Aplicativos instalados no projeto Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Adicione o nome do seu aplicativo 'app' aqui
    'crispy_forms',
    'django_filters',
]

# Configurações de URL principal
APPEND_NAMESPACE = True
ROOT_URLCONF = 'config.urls' 
WSGI_APPLICATION = 'config.wsgi.application'

# Middleware do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
