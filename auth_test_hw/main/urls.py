from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import custom_logout


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', next_page='index'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', views.register, name='register'),
]


