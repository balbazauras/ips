from service.viewsets import DataEntryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('DataEntry', DataEntryViewSet)

