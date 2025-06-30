from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', include('root.urls'), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    # re_path('favicon.ico',RedirectView.as_view(url='/static/favicon.ico')),
]
