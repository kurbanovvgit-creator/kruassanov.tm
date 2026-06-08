"""Resolve product/gallery images to local static URLs (offline-friendly)."""
import re
from pathlib import Path

from django.conf import settings
from django.templatetags.static import static

_UNSPLASH_RE = re.compile(
    r'https?://images\.unsplash\.com/photo-([a-f0-9]+-[a-f0-9]+)',
    re.I,
)


def static_images_dir() -> Path:
    return Path(settings.BASE_DIR) / 'static' / 'images'


def unsplash_id_from_url(url: str) -> str | None:
    match = _UNSPLASH_RE.search(url)
    return match.group(1) if match else None


def local_image_path(relative: str) -> str:
    """Normalize DB value to a path under static/, e.g. images/foo.jpg."""
    relative = (relative or '').strip().lstrip('/')
    if relative.startswith('static/'):
        relative = relative[7:]
    if not relative.startswith('images/'):
        relative = f'images/{relative}'
    return relative


def resolve_image_source(*, upload_field=None, path_or_url: str = '') -> str:
    """Return a URL suitable for <img src> — always prefers local static files."""
    if upload_field:
        return upload_field.url

    value = (path_or_url or '').strip()
    if not value:
        return ''

    if value.startswith(('http://', 'https://', '//')):
        photo_id = unsplash_id_from_url(value)
        if photo_id:
            return static(local_image_path(f'{photo_id}.jpg'))
        return value

    return static(local_image_path(value))
