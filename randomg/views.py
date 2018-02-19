# Create your views here.
from randomg.models import Quote
import random
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext


def generate(request):
    p = Quote.objects.all().count()
    primek = random.randint(1,p)
    x = get_object_or_404(Quote, pk=primek)
    return render(request, 'index.html',{'quote':x})
    # return render_to_response('index.html',{'quote':x},
    #                           context_instance=RequestContext(request))
    
