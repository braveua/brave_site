from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('root.urls'), name='index'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('admin/', admin.site.urls, name='admin'),
    # re_path('favicon.ico',RedirectView.as_view(url='/static/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
