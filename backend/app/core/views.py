from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Post,DeviceConfig

from rest_framework import viewsets

from .serializers import DeviceConfigSerializer

class DeviceConfigViewSet(viewsets.ModelViewSet):
    queryset = DeviceConfig.objects.all().order_by('device')
    serializer_class = DeviceConfigSerializer

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


# Create your views here.
