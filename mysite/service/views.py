from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .serializers import DataEntrySerializer
from .forms import CreateUserForm, SystemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    systems = request.user.technician.system_set.all()
    technician = request.user
    context = {
        'systems': systems,
        'technician': technician,
    }
    return render(request, 'service/home.html', context)


@login_required(login_url='login')
def sensor(request, pk):
    sensor = Sensor.objects.get(id=pk)
    data = sensor.dataentry_set.all()
    chartLabels = []
    chartData = []
    queryset = data.order_by('-date')[:20]
    #     %m/%d/%Y/%H/%M/%S/
    for query in queryset:
        chartLabels.append(query.date.strftime('%H:%M:%S'))
        chartData.append(query.value)
    context = {
        'sensor': sensor,
        'data': data,
        'chartLabels': chartLabels,
        'chartData': chartData
    }
    return render(request, 'service/sensor.html', context)


@login_required(login_url='login')
def system(request, pk):
    system = System.objects.get(id=pk)
    sensors = system.sensor_set.all()
    context = {
        'system': system,
        'sensors': sensors,
    }
    return render(request, 'service/system.html', context)


def createSystem(request, pk):
    technician = Technician.objects.get(id=pk)
    form = SystemForm(initial={'technician': technician})
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            print('Printing POST:', request.POST)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'service/create_system.html', context)


def updateSystem(request, pk):

    system = System.objects.get(id=pk)
    form = SystemForm(instance=system)

    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            form.save()
            print('Printing POST:', request.POST)
            return redirect('/')

    context = {'form': form}
    return render(request, 'service/update_system.html', context)


def deleteSystem(request, pk):
    system = System.objects.get(id=pk)
    if request.method == "POST":
        system.delete()
        return redirect('/')
    context = {'item': system}
    return render(request, 'service/delete_system.html', context)


def deleteSensor(request, pk):
    sensor = Sensor.objects.get(id=pk)
    if request.method == "POST":
        sensor.delete()
        return redirect('/')
    context = {'item': sensor}
    return render(request, 'service/delete_system.html', context)


def deleteDataEntry(request, pk):
    dataEntry = DataEntry.objects.get(id=pk)
    if request.method == "POST":
        dataEntry.delete()
        return redirect('/')
    context = {'item': dataEntry}
    return render(request, 'service/delete_dataentry.html', context)

# === Posting data from arduino


def postData(request):
    form = DataEntrySerializer
    context = {'form': form}
    return render(request, 'service/home.html', context)

 # ===Login/Register===


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if(request.method == 'POST'):
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'service/register.html', context)


def loginPage(request):
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


def logoutUser(request):
    logout(request)
    return redirect('login')
