
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('system/<str:pk>/', views.system, name="system_page"),
    path('create-system/<str:pk>/', views.create_system, name="create_system"),
    path('update-system/<str:pk>/', views.update_system, name="update_system"),
    path('delete-system/<str:pk>/', views.delete_system, name="delete_system"),
    path('sensor/<str:pk>/', views.sensor, name="sensor_page"),
    path('create-sensor/<str:pk>/', views.create_sensor, name="create_sensor"),
    path('update-sensor/<str:pk>/', views.update_sensor, name="update_sensor"),
    path('delete-sensor/<str:pk>/', views.delete_sensor, name="delete_sensor"),
    path('api/', include('api.urls'), name="api"),
]
