from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from core import views as core_views

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
]

handler404 = core_views.custom_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
