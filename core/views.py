from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Category, Product, Gallery


@require_GET
def home(request):
    featured_products = (
        Product.objects.filter(is_active=True, is_featured=True)
        .select_related('category')[:8]
    )
    if not featured_products.exists():
        featured_products = (
            Product.objects.filter(is_active=True).select_related('category')[:8]
        )
    categories = Category.objects.filter(is_active=True)[:6]
    return render(request, 'pages/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })


@require_GET
def catalog(request):
    categories = Category.objects.filter(is_active=True)
    selected_slug = request.GET.get('category')
    products_qs = (
        Product.objects.filter(is_active=True).select_related('category')
    )

    selected_category = None
    if selected_slug:
        selected_category = next(
            (c for c in categories if c.slug == selected_slug), None
        )
        if selected_category:
            products_qs = products_qs.filter(category=selected_category)

    return render(request, 'pages/catalog.html', {
        'categories': categories,
        'products': products_qs,
        'selected_category': selected_category,
    })


@require_GET
def about(request):
    return render(request, 'pages/about.html')


@require_GET
def gallery(request):
    items = Gallery.objects.filter(is_active=True)
    return render(request, 'pages/gallery.html', {'items': items})


@require_GET
def contacts(request):
    return render(request, 'pages/contacts.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
