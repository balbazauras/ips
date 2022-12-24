from django.contrib.auth.forms import UserCreationForm
from .models import Technician
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Technician
        fields = '__all__'


class SystemForm(forms.ModelForm):
    name = forms.CharField(
        label='System name:',
        widget=forms.TextInput(attrs={'placeholder': 'Packing conveyor'})
    )
    city = forms.CharField(
        label='City:',
        widget=forms.TextInput(attrs={'placeholder': 'Vilnius'})
    )
    company = forms.CharField(
        label='Company:',
        widget=forms.TextInput(attrs={'placeholder': 'Kauno baldai'})
    )
    building_or_plant = forms.CharField(
        label='Buidling or plant',
        widget=forms.TextInput(attrs={'placeholder': 'Packiging sector'})
    )
    description = forms.CharField(
        label='System discription:',
        widget=forms.TextInput()
    )
    manufacturer = forms.CharField(
        label='Systems manufacturer:',
        widget=forms.TextInput(attrs={'placeholder': 'SMC'})
    )

    date_next_inspection = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    inspection_interval = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    documentation = models.FileField(null=True)

    class Meta:
        model = System
        fields = '__all__'


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'
