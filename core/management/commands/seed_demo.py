"""Populate the database with demo data for the showcase site."""
from decimal import Decimal

from django.core.management.base import BaseCommand

from core.models import Category, Product, Gallery, SiteSettings


CATEGORIES = [
    {
        'name': 'Круассаны',
        'order': 1,
        'description': 'Слоёное тесто, выпеченное по классической рецептуре. '
                       'Хрустящая корочка и нежный мякиш.',
        'image_url': 'https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=1200&q=80',
    },
    {
        'name': 'Торты',
        'order': 2,
        'description': 'Авторские торты для особых случаев. '
                       'Натуральные ингредиенты, ручная сборка.',
        'image_url': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=1200&q=80',
    },
    {
        'name': 'Макаруны',
        'order': 3,
        'description': 'Французские макаруны — миндальная нежность '
                       'с воздушным кремом внутри.',
        'image_url': 'https://images.unsplash.com/photo-1558326567-98ae2405596b?w=1200&q=80',
    },
    {
        'name': 'Десерты',
        'order': 4,
        'description': 'Эклеры, тарты, муссовые пирожные — изысканные десерты '
                       'на каждый день.',
        'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80',
    },
    {
        'name': 'Напитки',
        'order': 5,
        'description': 'Кофе, авторские чаи, какао и фирменные напитки — '
                       'идеальное сопровождение для десертов.',
        'image_url': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=80',
    },
]


PRODUCTS = [
    # Круассаны
    ('Круассаны', 'Классический круассан', 18,
     'Слоёное тесто из французского масла, 36 часов расстойки.',
     '80 г', True,
     'https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=900&q=80'),
    ('Круассаны', 'Круассан с миндалём', 24,
     'Двойной выпеч с миндальным кремом франжипан и хлопьями миндаля.',
     '95 г', True,
     'https://images.unsplash.com/photo-1623334044303-241021148842?w=900&q=80'),
    ('Круассаны', 'Pain au chocolat', 22,
     'Слоёная булочка с двумя плитками тёмного бельгийского шоколада.',
     '85 г', False,
     'https://images.unsplash.com/photo-1600194992440-50b26c0a3f8d?w=900&q=80'),
    ('Круассаны', 'Круассан с фисташкой', 28,
     'Кремовая фисташковая начинка ручного приготовления.',
     '95 г', True,
     'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=900&q=80'),

    # Торты
    ('Торты', 'Fraisier', 240,
     'Лёгкий бисквит, ванильный крем муссолин и свежая клубника.',
     '1 кг', True,
     'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=900&q=80'),
    ('Торты', 'Opéra', 220,
     'Кофейный сливочный крем, ганаш и миндальный бисквит joconde.',
     '1 кг', True,
     'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=900&q=80'),
    ('Торты', 'Tarte au citron', 180,
     'Песочная основа и шелковистый лимонный курд с итальянской меренгой.',
     '900 г', False,
     'https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=900&q=80'),
    ('Торты', 'Чизкейк ваниль-бурбон', 200,
     'Сливочный сыр, мадагаскарская ваниль, песочная основа.',
     '1 кг', False,
     'https://images.unsplash.com/photo-1567327613485-fbc7bf196198?w=900&q=80'),

    # Макаруны
    ('Макаруны', 'Макарун малина', 14,
     'Миндальная меренга, ганаш с малиной из долины Дордонь.',
     '12 г', True,
     'https://images.unsplash.com/photo-1569864358642-9d1684040f43?w=900&q=80'),
    ('Макаруны', 'Макарун фисташка', 14,
     'Сицилийская фисташка, белый шоколад, миндаль.',
     '12 г', True,
     'https://images.unsplash.com/photo-1558326567-98ae2405596b?w=900&q=80'),
    ('Макаруны', 'Макарун ваниль', 14,
     'Мадагаскарская ваниль и тающий ганаш.',
     '12 г', False,
     'https://images.unsplash.com/photo-1612203985729-70726954388c?w=900&q=80'),
    ('Макаруны', 'Ассорти 12 шт.', 160,
     'Подарочная коробка с 12 макарунами всех вкусов.',
     '144 г', True,
     'https://images.unsplash.com/photo-1607920591413-4ec007e70023?w=900&q=80'),

    # Десерты
    ('Десерты', 'Éclair ваниль', 36,
     'Заварное тесто, ванильный крем патисьер, белая глазурь.',
     '90 г', True,
     'https://images.unsplash.com/photo-1612203985729-70726954388c?w=900&q=80'),
    ('Десерты', 'Tarte fraise', 42,
     'Хрустящая песочная корзинка, ванильный крем, свежая клубника.',
     '110 г', False,
     'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=900&q=80'),
    ('Десерты', 'Paris-Brest', 38,
     'Заварное кольцо с пралине и фундучной хрустящей крошкой.',
     '120 г', True,
     'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=900&q=80'),
    ('Десерты', 'Mille-feuille', 40,
     'Хрустящие слои с ванильным муссолином и сахарной пудрой.',
     '120 г', False,
     'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=900&q=80'),

    # Напитки
    ('Напитки', 'Espresso', 16,
     'Арабика тёмной обжарки, насыщенный вкус.',
     '40 мл', False,
     'https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=900&q=80'),
    ('Напитки', 'Капучино', 24,
     'Эспрессо и нежная молочная пена.',
     '200 мл', True,
     'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=900&q=80'),
    ('Напитки', 'Латте ваниль', 28,
     'Кофе с ванильным сиропом и шёлковым молоком.',
     '300 мл', False,
     'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=900&q=80'),
    ('Напитки', 'Горячий шоколад', 32,
     'Густой шоколадный напиток с какао-бобами single-origin.',
     '250 мл', True,
     'https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?w=900&q=80'),
]


GALLERY = [
    'https://images.unsplash.com/photo-1486427944299-d1955d23e34d?w=1400&q=80',
    'https://images.unsplash.com/photo-1464195244916-405fa0a82545?w=1400&q=80',
    'https://images.unsplash.com/photo-1517433670267-08bbd4be890f?w=1400&q=80',
    'https://images.unsplash.com/photo-1500917293891-ef795e70e1f6?w=1400&q=80',
    'https://images.unsplash.com/photo-1509440159596-0249088772ff?w=1400&q=80',
    'https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1400&q=80',
    'https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=1400&q=80',
    'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=1400&q=80',
    'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=1400&q=80',
    'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=1400&q=80',
    'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=1400&q=80',
    'https://images.unsplash.com/photo-1567327613485-fbc7bf196198?w=1400&q=80',
]


class Command(BaseCommand):
    help = 'Заполняет базу демонстрационными данными для витрины.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset', action='store_true',
            help='Удалить все категории, продукты и галерею перед заполнением.',
        )

    def _write(self, msg):
        """Write to stdout safely on consoles that can't encode unicode."""
        try:
            self.stdout.write(msg)
        except UnicodeEncodeError:
            enc = getattr(self.stdout._out, 'encoding', 'utf-8') or 'utf-8'
            self.stdout.write(msg.encode(enc, errors='replace').decode(enc))

    def handle(self, *args, **options):
        if options['reset']:
            Product.objects.all().delete()
            Category.objects.all().delete()
            Gallery.objects.all().delete()
            self._write('Old data removed.')

        SiteSettings.load()
        self._write('SiteSettings ready.')

        cat_count = 0
        for data in CATEGORIES:
            Category.objects.update_or_create(
                name=data['name'],
                defaults={
                    'order': data['order'],
                    'description': data['description'],
                    'image_url': data['image_url'],
                    'is_active': True,
                },
            )
            cat_count += 1
        self._write(f'Categories ensured: {cat_count}')

        prod_count = 0
        for cat_name, name, price, desc, weight, featured, image in PRODUCTS:
            category = Category.objects.get(name=cat_name)
            Product.objects.update_or_create(
                name=name,
                defaults={
                    'category': category,
                    'description': desc,
                    'price': Decimal(price),
                    'weight': weight,
                    'is_featured': featured,
                    'is_active': True,
                    'image_url': image,
                },
            )
            prod_count += 1
        self._write(f'Products ensured: {prod_count}')

        for index, url in enumerate(GALLERY, start=1):
            Gallery.objects.update_or_create(
                image_url=url,
                defaults={'order': index, 'is_active': True},
            )
        self._write(f'Gallery photos ensured: {len(GALLERY)}')

        self._write('\nDemo data is ready. Run: python manage.py runserver')
