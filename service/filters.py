import django_filters
from .models import Sensor
class SensorFilter(django_filters.FilterSet):
  
    class Meta:
        model=Sensor
        fields={'type':['exact'],
        'name':['icontains']}
        