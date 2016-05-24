from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import TrafficData, DeviceData
from .serializers import TrafficDataSerializer, DeviceDataSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    """
 An Http REsponse that renders its content to json
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
@api_view(['GET', 'POST'])
def device_list(request):
    """
 List all code snippets or create a new one

    """
    if request.method == 'GET':
        device = DeviceData.objects.all()
        serializer = DeviceDataSerializer(device, many=True)
        return JSONResponse(serializer.data)

nodelist = []
ininode = 0
finnode = 0

def coord(request, inicoord, fincoord):
    """
    function gets inicoord and fincoord as strings. they are first converted to get a list of floats,i.e.lat and lon

    """
    global ininode
    global finnode
    inicoord = inicoord.replace('[','')
    inicoord = inicoord.replace(']', '')
    inicoord = inicoord.split(',')
    inilat = float(inicoord[0])
    inilon = float(inicoord[1])
    ininodulus = DeviceData.objects.get(lat=inilat, lon=inilon)
    ininode = ininodulus.id
    initialcoordinates = [inilat,inilon]

    fincoord = fincoord.replace('[', '')
    fincoord = fincoord.replace(']', '')
    fincoord = fincoord.split(',')
    finlat = float(fincoord[0])
    finlon = float(fincoord[1])
    finnodulus = TrafficData.objects.get(lat=finlat, lon=finlon)
    finnode = finnodulus.id
    finalcoordinates = [finlat, finlon]

    context = {
        'initialcoordinates': initialcoordinates,
        'finalcoordinates': finalcoordinates,
    }

    return render(request,'androider/coord.html',context)

def dijk(request): #  to be used later

    for i in range(0, abs(finnode - ininode) + 1):
        c = DeviceData.objects.get(id = i)
        nodelist.append(c.id)

    return JSONResponse(nodelist)


