from django.http import HttpResponse
#from .models import Album
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.shortcuts import render_to_response
from django.template import RequestContext
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
#from flask import render_template


from django.http import Http404
from .models import soilfield

def recommend(rain, temp, irri):
    df = pd.read_csv('./data.csv')

    k_df = df[['Total Rainfall', 'Temperature', 'Need Irrigation']].as_matrix()

    scaler = StandardScaler().fit(k_df)
    k_df = scaler.transform(k_df)

    # rain = input("Enter rainfall in mm:")
    # temp = input("Enter temperature in degree Celsius:")
    # irri = input("Do you have irrigation?")

    if irri == 'y':
        ir = 1
    else:
        ir = 0

    new_mat = np.array([[rain, temp, ir]])
    new_mat = scaler.transform(new_mat)

    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(k_df)

    pred = neigh.kneighbors(new_mat, return_distance=False)
    return list(df.loc[pred[0]].loc[:,"Nepali Name"].values)

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

        st=recommend(2000, 13, 1)


        data=[area,dropdown,month,investment_min,investment_max,irri,timespan]


        return render_to_response('agri/form.html', {'st': st})

def second (request):
            #return HttpResponse("Milan tori mula")
            template = loader.get_template('agri/second.html')
            context = {
                'a': "area",
            }
            return HttpResponse(template.render(context, request))
