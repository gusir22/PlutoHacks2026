"""Deliberately insecure: LOCAL TRAINING ONLY. Never deploy."""
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='not-for-production-training-only'
DEBUG=True
ALLOWED_HOSTS=['localhost','127.0.0.1','testserver']
INSTALLED_APPS=['django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.staticfiles','lab']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware']
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request']}}]
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
