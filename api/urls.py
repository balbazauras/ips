from django.urls import path
from api import views
app_name = 'api'
urlpatterns = [
    path('', views.sensor_data, name="get_data"),
    path('get-all/', views.get_all_sensor_data, name="get_all_data"),
    path('get-params/', views.get_sensor_params, name="get_sensor_param"),
]
