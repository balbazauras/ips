from django.contrib import admin
from django.urls import path, include
from django.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
    path('api/', include('api.urls')),

]
