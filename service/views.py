from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, F
from rest_framework.decorators import api_view
from rest_framework import filters, generics
from rest_framework.filters import SearchFilter
from .serializers import SystemSerializer, SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import SystemFilter
from django.forms.models import model_to_dict
# Create your views here.


@login_required(login_url='login')
@api_view(['GET'])
def home(request):
    """Show systems assigned to technician"""
    if request.query_params.get('search') is not None:
        search = request.query_params.get('search')
        systems = request.user.system_set.all().filter(name__icontains=search)
    else:
        systems = request.user.system_set.all()
    context = {
        'systems': systems,
        'technician': request.user,
    }
    return render(request, 'service/home.html', context)


@login_required(login_url='login')
@api_view(['GET'])
def system(request, pk):
    """Shows sensors assigned to a single system """
    single_system = System.objects.get(id=pk)
    sensors = single_system.sensor_set.all()
    if request.query_params.get('q') is not None:
        q = request.query_params.get('q')
        sensors = sensors.filter(name__icontains=q)
    context = {
        'system': single_system,
        'sensors': sensors,
    }
    return render(request, 'service/system.html', context)


@login_required(login_url='login')
def sensor(request, pk):
    """Shows information about data entrys from single sensor """
    single_sensor = Sensor.objects.get(id=pk)
    sensor_data = single_sensor.dataentry_set.all().order_by('-arduino_date')
    number_of_entries = sensor_data.count()
    average_value = sensor_data.aggregate(
        Avg('value'))['value__avg']
    delta_time = sensor_data.aggregate(
        average_delta=Avg(F('server_date') - F('arduino_date')))
    object = model_to_dict(single_sensor)
    context = {
        'sensor': single_sensor,
        'data': sensor_data,
        'number_of_entries': number_of_entries,
        'average_value': average_value,
        'delta_time': delta_time['average_delta'],
        'object':object,
    }
    return render(request, 'service/sensor.html', context)


def create_system(request, pk):
    """Creates single system """
    technician = Technician.objects.get(id=pk)
    form = SystemForm(initial={'technician': technician})
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'service/create_system.html', context)


def update_system(request, pk):
    """Updates single system data fields"""
    single_system = System.objects.get(id=pk)
    form = SystemForm(instance=single_system)

    if request.method == 'POST':
        form = SystemForm(request.POST, request.FILES, instance=single_system)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'service/update_system.html', context)


def delete_system(request, pk):
    """Deletes single system using unique id"""
    single_system = System.objects.get(id=pk)
    if request.method == "POST":
        single_system.delete()
        return redirect('/')
    context = {'item': single_system}
    return render(request, 'service/delete_system.html', context)


def delete_sensor(request, pk):
    """Deletes single sensor using unique id"""
    single_sensor = Sensor.objects.get(id=pk)
    if request.method == "POST":
        single_sensor.delete()
        return redirect('/')
    context = {'item': single_sensor}
    return render(request, 'service/delete_system.html', context)


def delete_data_entry(request, pk):
    """Deletes single data entry using unique id"""
    data_entry = DataEntry.objects.get(id=pk)
    if request.method == "POST":
        data_entry.delete()
        return redirect('/')
    context = {'item': data_entry}
    return render(request, 'service/delete_dataentry.html', context)


def register_page(request):
    """ Registers user"""
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'service/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'service/login.html', context)


def logout_user(request):
    """ Log outs user"""
    logout(request)
    return redirect('login')


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'service/delete_dataentry.html')


def web_socket(request):
    return render(request, 'service/web.html')


def create_sensor(request, pk):
    """Creates single system """
    system = System.objects.get(id=pk)
    form = SensorForm(initial={'system': system})
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'service/create_sensor.html', context)


def update_sensor(request, pk):
    """Updates single system data fields"""
    single_sensor = Sensor.objects.get(id=pk)
    form = SensorForm(instance=single_sensor)

    if request.method == 'POST':
        form = SensorForm(request.POST, request.FILES, instance=single_sensor)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'service/update_sensor.html', context)


def delete_sensor(request, pk):
    """Deletes single system using unique id"""
    single_sensor = Sensor.objects.get(id=pk)
    if request.method == "POST":
        single_sensor.delete()
        return redirect('/')
    context = {'item': single_sensor}
    return render(request, 'service/delete_sensor.html', context)
