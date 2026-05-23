# Kruassanov.tm — Maison de pâtisserie

Демо-сайт-витрина для французской кондитерской `Kruassanov.tm`.  
Дизайн вдохновлён [Ladurée](https://laduree.com/): кремово-бежевая палитра,
крупная типографика Playfair Display, плавные анимации, премиальный UX.

## Технологии

- **Backend:** Django 5
- **Frontend:** Django Templates + TailwindCSS (CDN) + ванильный JavaScript
- **База данных:** SQLite
- **Шрифты:** Playfair Display + Inter (Google Fonts)
- **Статика в продакшене:** WhiteNoise

## Структура

```
kruassanov/
├── manage.py
├── requirements.txt
├── .env.example
├── kruassanov_site/         # настройки Django
├── core/                    # приложение: модели, админка, views, URL
│   ├── models.py            # Category, Product, Gallery, SiteSettings
│   ├── admin.py
│   ├── views.py
│   ├── context_processors.py
│   └── management/commands/
│       └── seed_demo.py     # наполнение демо-данными
├── templates/
│   ├── base.html
│   ├── 404.html
│   ├── components/
│   │   ├── navbar.html
│   │   └── footer.html
│   └── pages/
│       ├── home.html
│       ├── catalog.html
│       ├── about.html
│       ├── gallery.html
│       └── contacts.html
├── static/
│   ├── css/style.css        # luxury theme
│   └── js/main.js           # анимации, sticky nav, mobile menu
└── media/                   # пользовательские загрузки
```

## Запуск (Windows / PowerShell)

```powershell
# 1. Виртуальное окружение
python -m venv venv
venv\Scripts\Activate.ps1

# 2. Зависимости
pip install -r requirements.txt

# 3. Конфигурация
copy .env.example .env

# 4. Миграции
python manage.py makemigrations
python manage.py migrate

# 5. Демо-данные (категории, продукты, галерея)
python manage.py seed_demo

# 6. Суперпользователь для админки
python manage.py createsuperuser

# 7. Запуск сервера
python manage.py runserver
```

Сайт будет доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/),  
админка — [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Запуск (Linux / macOS)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

## Страницы

| URL              | Назначение                                             |
|------------------|--------------------------------------------------------|
| `/`              | Главная — hero, популярные десерты, категории, галерея |
| `/catalog/`      | Каталог с фильтром по категориям                       |
| `/about/`        | О компании                                             |
| `/gallery/`      | Полная галерея в стиле masonry                         |
| `/contacts/`     | Контакты + демо-форма + карта                          |
| `/admin/`        | Django Admin                                           |

## Django Admin

В админке доступны:

- **Настройки сайта** — singleton-объект `SiteSettings` (название компании,
  логотип, телефон, Instagram, адрес, hero-блок, текст «о нас», подвал).
- **Категории** — название, описание, изображение / URL-изображения, порядок.
- **Продукты** — категория, цена, валюта, вес, описание, изображение,
  флаги «популярный» и «активен».
- **Галерея** — фотографии с возможностью сортировки и активации.

Изображения можно либо загрузить файлом (`media/`), либо указать URL
(`image_url`) — это удобно для демо с фото с Unsplash.

## Переменные окружения (`.env`)

```ini
DJANGO_SECRET_KEY=change-me-to-a-very-long-random-string
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

## Продакшен

Чек-лист перед деплоем:

1. `DJANGO_DEBUG=False`, заполнить `DJANGO_ALLOWED_HOSTS`.
2. Сгенерировать новый `DJANGO_SECRET_KEY`.
3. `python manage.py collectstatic --noinput` (WhiteNoise отдаст статику).
4. Настроить раздачу `media/` через nginx / S3.
5. Для production-сборки Tailwind перейти с CDN на [standalone CLI](https://tailwindcss.com/blog/standalone-cli)
   и собрать `static/css/tailwind.css`.

## Лицензия

Демо-проект, свободно используйте и адаптируйте под свои нужды.
