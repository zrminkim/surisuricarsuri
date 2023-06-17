from pathlib import Path
import os

# 다음과 같이 프로젝트 내부에 경로를 빌드합니다: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 빠른 시작 개발 설정 - 프로덕션에 적합하지 않음
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 보안 경고: 생산에 사용된 비밀 키를 비밀로 유지하십시오!
SECRET_KEY = 'django-insecure-@7o+8j71k-3s)=k#5t%g95=n(66sf%hpg2im(8(^_7^*ne3)(9'

# 보안 경고: 프로덕션에서 디버그를 켠 상태로 실행하지 마십시오!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'carsuri',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carsuri', # DB:db는 미리 작성되어있어야 한다.
        'USER': 'root', # 계정명
        'PASSWORD': '123', # 계정 암호
        'HOST': '127.0.0.1', # DB가 설치된 PC의 IP
        'PORT': '3306', # DBMS의 port 번호
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# 웹페이지에 사용할 정적파일의 최상위 URL경로
STATIC_URL = '/static/'
#정적파일이 위치한 경로들을 지정하는 설정 항목
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# 각 media file에 대한 Root
MEDIA_URL = '/media/'
# 미디어 파일을 관리할 루트 media 디렉터리
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
