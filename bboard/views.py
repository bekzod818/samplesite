from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from django.shortcuts import render

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})
    
    
    # s = 'Reklamalar ro\'yhati\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type = 'text/plain; charset = utf-8')