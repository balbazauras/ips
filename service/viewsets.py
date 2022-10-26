from rest_framework import viewsets
from . import models
from . import serializers


class DataEntryViewSet(viewsets.ModelViewSet):
    queryset = models.DataEntry.objects.all()
    serializer_class = serializers.DataEntrySerializer
