from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def _ru_slug(value: str) -> str:
    """Slug from Cyrillic-safe name (falls back to id-based slug elsewhere)."""
    mapping = str.maketrans({
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    })
    transliterated = value.lower().translate(mapping)
    slug = slugify(transliterated)
    return slug or 'item'


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    """Singleton model for global site configuration."""
    company_name = models.CharField(
        'Название компании', max_length=120, default='Kruassanov'
    )
    tagline = models.CharField(
        'Подзаголовок шапки', max_length=200, blank=True,
        default='Maison de pâtisserie'
    )
    logo = models.ImageField('Логотип', upload_to='settings/', blank=True, null=True)

    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('E-mail', blank=True)
    instagram_url = models.URLField(
        'Instagram', blank=True,
        default='https://www.instagram.com/kruassanov.tm/'
    )
    address = models.CharField('Адрес', max_length=255, blank=True)
    working_hours = models.CharField('Часы работы', max_length=150, blank=True)

    hero_title = models.CharField(
        'Hero — заголовок', max_length=200,
        default="L'art de la pâtisserie"
    )
    hero_subtitle = models.CharField(
        'Hero — подзаголовок', max_length=300,
        default='Французская кондитерская — каждый десерт создан вручную с любовью.'
    )
    hero_button_text = models.CharField(
        'Hero — текст кнопки', max_length=60, default='Смотреть меню'
    )
    hero_image = models.ImageField(
        'Hero — фоновое изображение', upload_to='settings/', blank=True, null=True
    )
    hero_image_url = models.URLField(
        'Hero — URL изображения (если не загружено)', blank=True,
        default='https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=2000&q=80'
    )

    about_title = models.CharField(
        'О компании — заголовок', max_length=200,
        default='Искусство, рождённое во Франции'
    )
    about_text = models.TextField(
        'О компании — короткий текст',
        default=(
            'Kruassanov — это маленькая мастерская, где каждый день рождаются '
            'десерты по лучшим традициям французской кондитерской школы. '
            'Свежие ингредиенты, ручная работа и безупречный вкус.'
        )
    )
    about_image_url = models.URLField(
        'О компании — изображение URL', blank=True,
        default='https://images.unsplash.com/photo-1517433670267-08bbd4be890f?w=1600&q=80'
    )

    footer_text = models.CharField(
        'Текст подвала', max_length=300,
        default='© Kruassanov.tm — Maison de pâtisserie'
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Category(TimeStampedModel):
    name = models.CharField('Название', max_length=120, unique=True)
    slug = models.SlugField('Slug', max_length=140, unique=True, blank=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField(
        'Изображение', upload_to='categories/', blank=True, null=True
    )
    image_url = models.URLField(
        'URL изображения (используется если файл не загружен)', blank=True
    )
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _ru_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"{reverse('core:catalog')}?category={self.slug}"

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products',
        verbose_name='Категория'
    )
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Slug', max_length=220, unique=True, blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField(
        'Цена', max_digits=10, decimal_places=2, default=0
    )
    currency = models.CharField('Валюта', max_length=8, default='TMT')
    weight = models.CharField(
        'Вес / порция', max_length=50, blank=True,
        help_text='Например: 80 г, 6 шт.'
    )
    image = models.ImageField(
        'Изображение', upload_to='products/', blank=True, null=True
    )
    image_url = models.URLField(
        'URL изображения (используется если файл не загружен)', blank=True
    )
    is_featured = models.BooleanField('Популярный', default=False)
    is_active = models.BooleanField('Активен', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ('order', '-created_at')
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = _ru_slug(self.name)
            slug = base
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f'{base}-{i}'
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class Gallery(TimeStampedModel):
    title = models.CharField('Подпись', max_length=200, blank=True)
    image = models.ImageField(
        'Изображение', upload_to='gallery/', blank=True, null=True
    )
    image_url = models.URLField(
        'URL изображения (используется если файл не загружен)', blank=True
    )
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        ordering = ('order', '-created_at')
        verbose_name = 'Фото в галерее'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title or f'Photo #{self.pk}'

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url
