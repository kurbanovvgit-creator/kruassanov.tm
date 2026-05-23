from .models import SiteSettings, Category


def site_settings(request):
    return {'site_settings': SiteSettings.load()}


def navigation(request):
    return {
        'nav_links': [
            {'label': 'Главная', 'url_name': 'core:home'},
            {'label': 'Каталог', 'url_name': 'core:catalog'},
            {'label': 'О нас', 'url_name': 'core:about'},
            {'label': 'Галерея', 'url_name': 'core:gallery'},
            {'label': 'Контакты', 'url_name': 'core:contacts'},
        ],
        'nav_categories': Category.objects.filter(is_active=True),
    }
