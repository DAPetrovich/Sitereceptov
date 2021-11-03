# Сервис кулинарнах рецептов

Сервис кулинарнах рецептов.

## Использование Docker

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.dist .env
```

Внесите при необходимости корректировки в переменные окружения.

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров
Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта
Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```

#### создание миграций применять только при разработке:
```bash
python ./manage.py makemigrations receptsite
```

#### Применение миграций:
```bash
python ./manage.py migrate
```

#### Сборка статики:
```bash
python ./manage.py collectstatic
```

#### Создание суперпользователя
```bash
python ./manage.py createsuperuser
```

#### Создание фикструр. Только при сохранении данных. при установке не нужно
```bash
python ./manage.py dumpdata receptsite.Bludo --indent 2 > receptsite/fixtures/Bludo.json
python ./manage.py dumpdata receptsite.Ingredient --indent 2 > receptsite/fixtures/Ingredient.json
```

#### Добавление фикстур (Загрузка тестовых данных в базу)
```bash
python ./manage.py loaddata Bludo Ingredient
```

Проект доступен по адресу http://127.0.0.1:8000
