from django.contrib.auth.forms import UserCreationForm
from .models import Technician
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Technician
        fields = ("username", "password1", "password2")


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
    class Meta:
        model = System
        fields = '__all__'


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'
