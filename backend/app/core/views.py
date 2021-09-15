from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Sample


def index(request):
    samples = Sample.objects.order_by('attachment')[:5]
    template = loader.get_template('index.html')
    context = {
        'samples': samples,
    }
    return HttpResponse(template.render(context, request))


# Create your views here.
