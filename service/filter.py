import django_filters
from .models import Sensor, System


class SystemFilter(django_filters.FilterSet):

    class Meta:
        model = System
        fields = ('name', 'manufacturer')
