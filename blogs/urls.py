from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('login/', views.login_view, name='login'),
    path('logoff/', views.logoff, name='logoff'),
]