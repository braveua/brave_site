## Установка UV
```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

## Создание пустого проекта
в новом каталоге сайта (/home/brave/webdev/brave.it)
создаем новый проект
```bash
uv init --name="brave.it" .
```

получаем структуру:
```
.
├── .git
├── .gitignore
├── main.py
├── pyproject.toml
├── .python-version
├── README.md
└── uv.lock
```

## Устанавливаем библиотеки
```bash
uv add django==5.2 oracledb==3.1.0 gunicorn==23.0.0
```


## Создаем проект
```bash
uv run django-admin startproject braveit .
```

## Создаем каталог для статических файлов
```bash
mkdir static
```

## Добавляем переменные в систему
/home/user/.bashrc 
```ini
export ORA_TNS="ora_x23"
export ORA_USER="superadmin"
export ORA_PASSWORD="superadmin password"
export ORA_NAME="192.168.0.10:1521/freepdb1"

```

## settings.py
```python
import os
# Настройки БД ORACLE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": os.environ.get("ORA_NAME"),
        "USER": os.environ.get("ORA_USER"),
        "PASSWORD": os.environ.get("ORA_PASSWORD")
    },
        "ORA_CR": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": os.environ.get("ORA_NAME"),
        "USER": os.environ.get("ORA_CR_USER"),
        "PASSWORD": os.environ.get("ORA_CR_PASSWORD")
    },

# добавляем свое приложение "root"
INSTALLED_APPS = [
    "старые приложения",
    "root",
]


}
DATABASE_ROUTERS = ['routers.RootRouter']
#DATABASE_ROUTERS = ['app.routers.RootRouter']

#Доступность сайта
ALLOWED_HOSTS = ["*"]

#путь к static
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/',]
```


## Создаем роутер для БД
braveit/router.py
```python
class RootRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('nbu'):
            return 'ORA_CR'
        return None

```

## Добавляем пути приложений в /braveit/urls.py
```python
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', include('root.urls'), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    # re_path('favicon.ico',RedirectView.as_view(url='/static/favicon.ico')),
]

```