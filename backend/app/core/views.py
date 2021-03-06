import time
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response
from rest_framework.decorators import api_view



from django.utils.datastructures import MultiValueDictKeyError

from .models import DeviceConfig,SensorReading,Device,Sample

from rest_framework import viewsets

from .serializers import DeviceConfigSerializer,DeviceSerializer,SensorReadingSerializer,SampleSerializer,UserSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all().order_by('-id')
    lookup_field = 'device'
    serializer_class = SampleSerializer
    def retrieve(self,request,device):
        return Response(self.serializer_class(Sample.objects.filter(device=device).order_by('-id').first()).data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated,  ]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceConfigViewSet(viewsets.ModelViewSet):
    #todo: secure
    authentication_classes = []
    queryset = DeviceConfig.objects.all().order_by('device')
    def get_queryset(self):
        device = self.get_renderer_context()["request"].query_params.get('device')
        if device:
            print("it got called")
            return DeviceConfig.objects.filter(device=Device(device=device))[0:]
        else:
            return self.queryset
    serializer_class = DeviceConfigSerializer

class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all().order_by('device')
    serializer_class = SensorReadingSerializer
    
    def get_queryset(self):
        #if we've defined a device, just get it's sensor readings. otherwise get everything
        try:
            device = self.get_renderer_context()["request"].query_params['device']
            ledState = self.get_renderer_context()["request"].query_params.get('ledState')
            pumpState = self.get_renderer_context()["request"].query_params.get('pumpState')
            solenoidState = self.get_renderer_context()["request"].query_params.get('solenoidState')
            psi = self.get_renderer_context()["request"].query_params.get('psi')
            #TODO: this currently isn't working, and is falling though to the exception handler
            if (all(v is None for v in [ledState,solenoidState,pumpState,psi])):
                print("lols")
                return SensorReading.objects.filter(device=Device(id=device))[:600:-1]
            else:
                #if we're updating the entire set of variables, no need to get the most recent readings
                if all([ledState,solenoidState,pumpState,psi]):
                    obj = SensorReading(
                    device=Device(id=device),
                    ledState=ledState,
                    solenoidState=bool(solenoidState),
                    pumpState=bool(pumpState),
                    psi=psi)
                    obj.save()
                    return [obj]
                else: #TODO:otherwise we'll get the most recen
                    #last =SensorReading.objects.filter(device).latest()
                    #obj = SensorReading.objects.create(
                    #    ledState if ledState else last.get
                    #)
                    #obj = SensorReading.objects.create(device,ledState,solenoidState,pumpState,psi)
                    print([ledState,solenoidState,pumpState,psi])

                    return SensorReading.objects.all().order_by('-time')[:600:-1]
        #TODO: add specificity to this handler
        except MultiValueDictKeyError as e: #if the device ID isn't found in the request, get all the objects
            return SensorReading.objects.all().order_by('-time')[:600:-1]



def index(request):
    devices = Device.objects.all()[:5]
    template = loader.get_template('index.html')
    context = {
        'posts': devices,
    }
    return HttpResponse(template.render(context, request))

#TODO: secure this endpoint
@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES['files']:
        upload = request.FILES['files']
        device = request.POST['device']
        fss = FileSystemStorage()
        uname = str(time.time()) + upload.name
        file = fss.save(uname, upload)
        file_url = fss.url(file)
        Sample.objects.create(attachment=uname,device=Device.objects.get(id=device))
        return HttpResponse({file_url})
    return request

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
