from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Worker


def home(request):
    try:
        top_workers = Worker.objects.order_by('experience')[:5].reverse()
    except IndexError:
        top_workers = Worker.objects.order_by('experience').all().reverse()
    return render_to_response('index.html', {'top_workers': top_workers}, RequestContext(request))

