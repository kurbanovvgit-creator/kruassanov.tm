"""Download demo images from Unsplash into static/images/ for offline use."""
import urllib.error
import urllib.request
from pathlib import Path

from django.core.management.base import BaseCommand

from core.offline_assets import static_images_dir, unsplash_id_from_url

# All photo IDs used across seed data and page templates.
PHOTO_IDS = [
    '1461023058943-07fcbe16d735',
    '1464195244916-405fa0a82545',
    '1486427944299-d1955d23e34d',
    '1488477181946-6428a0291777',
    '1495474472287-4d71bcdd2085',
    '1500917293891-ef795e70e1f6',
    '1509440159596-0249088772ff',
    '1510707577719-ae7c14805e3a',
    '1517433670267-08bbd4be890f',
    '1519915028121-7d3463d20b13',
    '1542990253-0d0f5be5f0ed',
    '1551024506-0bccd828d307',
    '1555507036-ab1f4038808a',
    '1558326567-98ae2405596b',
    '1563729784474-d77dbb933a9e',
    '1565958011703-44f9829ba187',
    '1567327613485-fbc7bf196198',
    '1568376794508-ae52c6ab3929',
    '1569864358642-9d1684040f43',
    '1578985545062-69928b1d9587',
    '1600194992440-50b26c0a3f8d',
    '1606312619070-d48b4c652a52',
    '1606313564200-e75d5e30476c',
    '1607920591413-4ec007e70023',
    '1612203985729-70726954388c',
    '1623334044303-241021148842',
]

UNSPLASH_URLS = [
    f'https://images.unsplash.com/photo-{photo_id}?w=1400&q=80'
    for photo_id in PHOTO_IDS
]


class Command(BaseCommand):
    help = 'Скачивает демо-изображения в static/images/ для работы без интернета.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force', action='store_true',
            help='Перезаписать уже существующие файлы.',
        )

    def handle(self, *args, **options):
        images_dir = static_images_dir()
        images_dir.mkdir(parents=True, exist_ok=True)

        downloaded = 0
        skipped = 0
        failed = 0

        for url in UNSPLASH_URLS:
            photo_id = unsplash_id_from_url(url)
            if not photo_id:
                self.stderr.write(f'Skip invalid URL: {url}')
                failed += 1
                continue

            dest = images_dir / f'{photo_id}.jpg'
            if dest.exists() and not options['force']:
                skipped += 1
                continue

            try:
                request = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'KruassanovDemo/1.0'},
                )
                with urllib.request.urlopen(request, timeout=60) as response:
                    dest.write_bytes(response.read())
                downloaded += 1
                self.stdout.write(f'Downloaded: {dest.name}')
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                failed += 1
                self.stderr.write(f'Failed {photo_id}: {exc}')

        self.stdout.write(
            f'\nDone. Downloaded: {downloaded}, skipped: {skipped}, failed: {failed}'
        )
        if failed:
            self.stdout.write(
                'Some images failed — re-run when online or copy files into static/images/.'
            )
