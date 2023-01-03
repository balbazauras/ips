from rest_framework import serializers
from service.models import DataEntry, Sensor


class DataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['value_upper', 'value_lower', 'check_interval','normal_interval']
