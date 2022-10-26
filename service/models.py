from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Technician(AbstractUser):
    phone_number = models.IntegerField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "technician"
        verbose_name_plural = "technicians"
        db_table = "technician"


class System(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    date_next_inspection = models.DateTimeField(null=True)
    inspection_interval = models.DateTimeField(null=True)
    location = models.CharField(max_length=200, null=True)
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    documentation = models.FileField(blank=True, upload_to='documentation/')

    def __str__(self):
        return self.name


class Sensor(TimeStampedModel):
    TYPES = (
        ('Pressure', 'Pressure'),
        ('Tempreture', 'Tempreture'),
        ('Distance', 'Distance'),
        ('Humidity', 'Humidity'),
        ('Proximity', 'Proximity'),
        ('Gyroscope', 'Gyroscope'),
        ('Optical', 'Optical'),
        ('Accelerometer', 'Accelerometer'),
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=200, null=True, blank=True)
    date_of_installation = models.DateTimeField(null=True)
    type = models.CharField(max_length=200, choices=TYPES, null=True)
    system = models.ForeignKey(System, on_delete=models.DO_NOTHING)
    value_lower = models.DecimalField(
        decimal_places=2, max_digits=10, null=True)
    value_upper = models.DecimalField(
        decimal_places=2, max_digits=10, null=True)
    interval = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images/')
    documentation = models.FileField(blank=True, upload_to='documentation/')

    def __str__(self):
        return self.name


class DataEntry(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=10)
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    arduino_date = models.DateTimeField(blank=True, null=True)
    server_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)
