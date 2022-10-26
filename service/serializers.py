from .models import DataEntry
from django.forms import ModelForm
from rest_framework import serializers


class DataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = '__all__'
