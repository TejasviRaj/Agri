from django.http import HttpResponse
#from .models import Album
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.shortcuts import render_to_response
from django.template import RequestContext
#from flask import render_template


from django.http import Http404
from .models import soilfield

def index (request):

    # for unordered listing using commas
    #all_albums= Album.objects.order_by('-artist')[:5]
    #output = ', '.join([q.artist for q in all_albums])
    #return HttpResponse(output)

    #for ordered listing with index.html
    #all_albums= Album.objects.order_by('-artist')[:5]
    #all_albums= Album.objects.all
    #context={'harke':all_albums,}

    #album = get_object_or_404(Album,pk=album_id)
    #return render(request,"agri/detail.html", {'ram':album})
    #return HttpResponse("Singer %s " % album_id)


    #template=loader.get_template('agri/index.html')
    #return HttpResponse(template.render(context,request))
    #a = soilfield.objects.order_by('-area')[:5]
    template = loader.get_template('agri/index.html')
    context = {
        'a': "area",
    }
    return HttpResponse(template.render(context, request))

def submit (request):

    if request.method == 'POST':
        area=request.POST.get("Area", "")
        dropdown=request.POST.get("dropdown", "")
        month=request.POST.get("month", "")
        investment_min=request.POST.get("investment_min", "")
        investment_max=request.POST.get("investment_max", "")
        irri=request.POST.get("irrigation", "")
        timespan=request.POST.get("timespan", "")

        data=[area,dropdown,month,investment_min,investment_max,irri,timespan]

        return render_to_response('agri/form.html', {'data': data})

def second (request):
            #return HttpResponse("Milan tori mula")
            template = loader.get_template('agri/second.html')
            context = {
                'a': "area",
            }
            return HttpResponse(template.render(context, request))
