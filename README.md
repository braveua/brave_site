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
}

#Доступность сайта
ALLOWED_HOSTS = ["*"]

#путь к static
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/',]
```
