from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('login/', views.login_view, name='login'),
    path('logoff/', views.logoff, name='logoff'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    # path('home/', views.home, name='home'),
]