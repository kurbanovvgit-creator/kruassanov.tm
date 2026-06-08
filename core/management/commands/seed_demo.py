"""Populate the database with demo data for the showcase site."""
from decimal import Decimal

from django.core.management.base import BaseCommand

from core.models import Category, Product, Gallery, SiteSettings


def _img(photo_id: str) -> str:
    return f'images/{photo_id}.jpg'


CATEGORIES = [
    {
        'name': 'Круассаны',
        'order': 1,
        'description': 'Слоёное тесто, выпеченное по классической рецептуре. '
                       'Хрустящая корочка и нежный мякиш.',
        'image_url': _img('1555507036-ab1f4038808a'),
    },
    {
        'name': 'Торты',
        'order': 2,
        'description': 'Авторские торты для особых случаев. '
                       'Натуральные ингредиенты, ручная сборка.',
        'image_url': _img('1578985545062-69928b1d9587'),
    },
    {
        'name': 'Макаруны',
        'order': 3,
        'description': 'Французские макаруны — миндальная нежность '
                       'с воздушным кремом внутри.',
        'image_url': _img('1558326567-98ae2405596b'),
    },
    {
        'name': 'Десерты',
        'order': 4,
        'description': 'Эклеры, тарты, муссовые пирожные — изысканные десерты '
                       'на каждый день.',
        'image_url': _img('1488477181946-6428a0291777'),
    },
    {
        'name': 'Напитки',
        'order': 5,
        'description': 'Кофе, авторские чаи, какао и фирменные напитки — '
                       'идеальное сопровождение для десертов.',
        'image_url': _img('1495474472287-4d71bcdd2085'),
    },
]


PRODUCTS = [
    # Круассаны
    ('Круассаны', 'Классический круассан', 18,
     'Слоёное тесто из французского масла, 36 часов расстойки.',
     '80 г', True, _img('1555507036-ab1f4038808a')),
    ('Круассаны', 'Круассан с миндалём', 24,
     'Двойной выпеч с миндальным кремом франжипан и хлопьями миндаля.',
     '95 г', True, _img('1623334044303-241021148842')),
    ('Круассаны', 'Pain au chocolat', 22,
     'Слоёная булочка с двумя плитками тёмного бельгийского шоколада.',
     '85 г', False, _img('1600194992440-50b26c0a3f8d')),
    ('Круассаны', 'Круассан с фисташкой', 28,
     'Кремовая фисташковая начинка ручного приготовления.',
     '95 г', True, _img('1509440159596-0249088772ff')),

    # Торты
    ('Торты', 'Fraisier', 240,
     'Лёгкий бисквит, ванильный крем муссолин и свежая клубника.',
     '1 кг', True, _img('1578985545062-69928b1d9587')),
    ('Торты', 'Opéra', 220,
     'Кофейный сливочный крем, ганаш и миндальный бисквит joconde.',
     '1 кг', True, _img('1565958011703-44f9829ba187')),
    ('Торты', 'Tarte au citron', 180,
     'Песочная основа и шелковистый лимонный курд с итальянской меренгой.',
     '900 г', False, _img('1519915028121-7d3463d20b13')),
    ('Торты', 'Чизкейк ваниль-бурбон', 200,
     'Сливочный сыр, мадагаскарская ваниль, песочная основа.',
     '1 кг', False, _img('1567327613485-fbc7bf196198')),

    # Макаруны
    ('Макаруны', 'Макарун малина', 14,
     'Миндальная меренга, ганаш с малиной из долины Дордонь.',
     '12 г', True, _img('1569864358642-9d1684040f43')),
    ('Макаруны', 'Макарун фисташка', 14,
     'Сицилийская фисташка, белый шоколад, миндаль.',
     '12 г', True, _img('1558326567-98ae2405596b')),
    ('Макаруны', 'Макарун ваниль', 14,
     'Мадагаскарская ваниль и тающий ганаш.',
     '12 г', False, _img('1612203985729-70726954388c')),
    ('Макаруны', 'Ассорти 12 шт.', 160,
     'Подарочная коробка с 12 макарунами всех вкусов.',
     '144 г', True, _img('1607920591413-4ec007e70023')),

    # Десерты
    ('Десерты', 'Éclair ваниль', 36,
     'Заварное тесто, ванильный крем патисьер, белая глазурь.',
     '90 г', True, _img('1612203985729-70726954388c')),
    ('Десерты', 'Tarte fraise', 42,
     'Хрустящая песочная корзинка, ванильный крем, свежая клубника.',
     '110 г', False, _img('1488477181946-6428a0291777')),
    ('Десерты', 'Paris-Brest', 38,
     'Заварное кольцо с пралине и фундучной хрустящей крошкой.',
     '120 г', True, _img('1551024506-0bccd828d307')),
    ('Десерты', 'Mille-feuille', 40,
     'Хрустящие слои с ванильным муссолином и сахарной пудрой.',
     '120 г', False, _img('1606312619070-d48b4c652a52')),

    # Напитки
    ('Напитки', 'Espresso', 16,
     'Арабика тёмной обжарки, насыщенный вкус.',
     '40 мл', False, _img('1510707577719-ae7c14805e3a')),
    ('Напитки', 'Капучино', 24,
     'Эспрессо и нежная молочная пена.',
     '200 мл', True, _img('1495474472287-4d71bcdd2085')),
    ('Напитки', 'Латте ваниль', 28,
     'Кофе с ванильным сиропом и шёлковым молоком.',
     '300 мл', False, _img('1461023058943-07fcbe16d735')),
    ('Напитки', 'Горячий шоколад', 32,
     'Густой шоколадный напиток с какао-бобами single-origin.',
     '250 мл', True, _img('1542990253-0d0f5be5f0ed')),
]


GALLERY = [
    _img('1486427944299-d1955d23e34d'),
    _img('1464195244916-405fa0a82545'),
    _img('1517433670267-08bbd4be890f'),
    _img('1500917293891-ef795e70e1f6'),
    _img('1509440159596-0249088772ff'),
    _img('1488477181946-6428a0291777'),
    _img('1563729784474-d77dbb933a9e'),
    _img('1551024506-0bccd828d307'),
    _img('1606313564200-e75d5e30476c'),
    _img('1606312619070-d48b4c652a52'),
    _img('1565958011703-44f9829ba187'),
    _img('1567327613485-fbc7bf196198'),
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

        settings = SiteSettings.load()
        settings.hero_image_url = _img('1555507036-ab1f4038808a')
        settings.about_image_url = _img('1517433670267-08bbd4be890f')
        settings.save()
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

        for index, path in enumerate(GALLERY, start=1):
            Gallery.objects.update_or_create(
                order=index,
                defaults={'image_url': path, 'is_active': True},
            )
        self._write(f'Gallery photos ensured: {len(GALLERY)}')

        self._write('\nDemo data is ready. Run: python manage.py runserver')
