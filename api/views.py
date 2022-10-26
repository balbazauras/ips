from rest_framework.response import Response
from rest_framework.decorators import api_view
from service.models import DataEntry
from .serializers import DataEntrySerializer

# Create your views here.


@api_view(['GET', 'POST'])
def sensor_data(request):
    if request.method == 'GET':
        sensor_id = request.query_params.get('sensor-id')
        number_start = request.query_params.get('number-start')
        number_end = request.query_params.get('number-end')
        date_start = request.query_params.get('date-start')
        date_end = request.query_params.get('date-end')
        filtered_data = DataEntry.objects.filter(value__gt=number_start, value__lt=number_end,
                                                 sensor__exact=sensor_id,
                                                 arduino_date__gt=date_start, arduino_date__lt=date_end
                                                 )
        serializer = DataEntrySerializer(filtered_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DataEntrySerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
def get_all_sensor_data(request):
    if request.method == 'GET' and 'number_of_values' in request.GET:
        sensor_id = request.query_params.get('sensor-id')
        number_of_values = request.query_params.get('number_of_values')
        filtered_data = DataEntry.objects.filter(
            sensor__exact=sensor_id).order_by('-date')[:int(number_of_values)]
        serializer = DataEntrySerializer(filtered_data, many=True)
        return Response(serializer.data)
    elif request.method == 'GET':
        sensor_id = request.query_params.get('sensor-id')
        filtered_data = DataEntry.objects.filter(sensor__exact=sensor_id)
        serializer = DataEntrySerializer(filtered_data, many=True)
        return Response(serializer.data)
