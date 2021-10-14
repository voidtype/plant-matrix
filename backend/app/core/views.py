import time
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage

from django.views.decorators.csrf import csrf_exempt, csrf_protect


from django.utils.datastructures import MultiValueDictKeyError

from .models import Post,DeviceConfig,SensorReading,Device,Sample

from rest_framework import viewsets

from .serializers import DeviceConfigSerializer,SensorReadingSerializer


class DeviceConfigViewSet(viewsets.ModelViewSet):
    queryset = DeviceConfig.objects.all().order_by('device')
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
            if (all(v is None for v in [ledState,solenoidState,pumpState,psi])):
                print("lols")
                return SensorReading.objects.filter(device=Device(id=device))
            else:
                #if we're updating the entire set of variables, no need to get the most recent readings
                if all([ledState,solenoidState,pumpState,psi]):
                    obj = SensorReading(
                    device=Device(id=device),
                    ledState=bool(ledState),
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

                    return SensorReading.objects.all()
        #TODO: add specificity to this handler
        except MultiValueDictKeyError as e: #if the device ID isn't found in the request, get all the objects
            return SensorReading.objects.all()


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

def index(request):
    posts = Post.objects.all()[:5]
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

#TODO: secure this endpoint
@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES['files']:
        upload = request.FILES['files']
        fss = FileSystemStorage()
        uname = str(time.time()) + upload.name
        file = fss.save(uname, upload)
        file_url = fss.url(file)
        Sample.objects.create(attachment=uname)
        return HttpResponse({file_url})
    return request

# Create your views here.
