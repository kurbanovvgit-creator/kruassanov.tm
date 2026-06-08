from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Gallery, SiteSettings


class _ImagePreviewMixin:
    image_field_name = 'image'
    url_field_name = 'image_url'

    def image_preview(self, obj):
        if hasattr(obj, 'display_image'):
            url = obj.display_image
        else:
            src = getattr(obj, self.image_field_name, None)
            url = src.url if src else getattr(obj, self.url_field_name, '')
        if not url:
            return '—'
        return format_html(
            '<img src="{}" style="height:60px;width:60px;object-fit:cover;'
            'border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.1);" />',
            url,
        )

    image_preview.short_description = 'Превью'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Компания', {
            'fields': ('company_name', 'tagline', 'logo'),
        }),
        ('Контакты', {
            'fields': ('phone', 'email', 'instagram_url', 'address',
                       'working_hours'),
        }),
        ('Hero-секция', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_button_text',
                       'hero_image', 'hero_image_url'),
        }),
        ('О компании', {
            'fields': ('about_title', 'about_text', 'about_image_url'),
        }),
        ('Подвал', {
            'fields': ('footer_text',),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(_ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'order', 'is_active', 'updated_at')
    list_display_links = ('image_preview', 'name')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    prepopulated_fields = {}
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'order', 'is_active'),
        }),
        ('Изображение', {
            'fields': ('image', 'image_url', 'image_preview'),
        }),
    )


@admin.register(Product)
class ProductAdmin(_ImagePreviewMixin, admin.ModelAdmin):
    list_display = (
        'image_preview', 'name', 'category', 'price', 'currency',
        'is_featured', 'is_active', 'order',
    )
    list_display_links = ('image_preview', 'name')
    list_editable = ('order', 'is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    autocomplete_fields = ('category',)
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'description', 'weight'),
        }),
        ('Цена', {
            'fields': ('price', 'currency'),
        }),
        ('Изображение', {
            'fields': ('image', 'image_url', 'image_preview'),
        }),
        ('Отображение', {
            'fields': ('is_featured', 'is_active', 'order'),
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(_ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'order', 'is_active', 'created_at')
    list_display_links = ('image_preview', 'title')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('title', 'order', 'is_active'),
        }),
        ('Изображение', {
            'fields': ('image', 'image_url', 'image_preview'),
        }),
    )
