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

def detail (request):

#    for key, value in request.POST.items():
#        print(key, value)
#    if (request.POST):
#        return render_to_response('agri/form.html')
    if request.method == 'POST':

        """
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            # render?
            return HttpResponseRedirect('/results/', {
                'restaurant': get_object_or_404(
                                                Restaurant,
                                                Area=request.POST['Area'],
                                                irrigation=request.POST['irrigation']
                                                )
                })
        """
        area=request.POST.get("Area", "")
        irri=request.POST.get("irrigation", "")
        data=[area,irri]
        #return render_to_response('agri/form.html', {'area': area},{'irri':irri})
        return render_to_response('agri/form.html', {'data': data})

def second (request):
            return HttpResponse("Milan tori mula")
