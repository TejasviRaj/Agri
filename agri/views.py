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

def recommend(rain, temp, irri, alt, month, timespan, area):
    df = pd.read_csv('./data.csv')

    if timespan == "three":
        df = df[df["Harvesting months"]==3]
    elif timespan == "six":
        df = df[df["Harvesting months"]==6]
    else:
        df = df[df["Harvesting months"]==12]

    ok_months = [x+int(month)-2 for x in range(5)]

    df_ind = []

    for n, m in enumerate(ok_months):
        if m < 1:
            ok_months[n] += 12
        if m > 12:
            ok_months[n] -= 12

    for i, mth in zip(df.index, df["Best month to harvest"]):
        if int(mth) in ok_months:
            df_ind.append(i)

    df = df.loc[df_ind]

    df = df[df["Max. Elevation (m)"] > alt]
    df = df[df["Min. Elevation (m)"] < alt]

    k_df = df[['Total Rainfall (mm)', 'Temperature', 'Need Irrigation']]

    scaler = StandardScaler().fit(k_df)
    k_df = scaler.transform(k_df)

    if irri[0] == 'y':
        ir = 1
    else:
        ir = 0

    new_mat = np.array([[rain, temp, ir]])
    new_mat = scaler.transform(new_mat)

    neigh = NearestNeighbors(n_neighbors=3)
    neigh.fit(k_df)

    pred = neigh.kneighbors(new_mat, return_distance=False)

    out = df.iloc[pred[0]].loc[:, ['Nepali Name', 'Investment per meter square', 'Market Price and returns per square meter']].values

    for n, x in enumerate(out):
        out[n] = [x[0], x[1]*int(area), x[2]*int(area)]
    return out.tolist()

def index (request):

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
        irri=request.POST.get("irrigation", "")
        timespan=request.POST.get("timespan", "")

        if area=="ana":
            area = 31.79*area
        elif area=="bigah":
            area = 6772.4*area
        try:
            st=list(recommend(1711, 16.7, irri, 1553, month, timespan, area))

        except ValueError:
            a="a"
            return render_to_response('agri/exception.html', {'a': a})

        for i in st:
            if i[0]=="Pea":
                i.append("﻿केराऊ")
            elif i[0]=="Sugarcane":
                i.append("उखु")
            elif i[0]=="Pineapple":
                i.append("भुइँकटहर")
            elif i[0]=="Broccoli":
                i.append("ब्रोकोली")
            elif i[0]=="Amba":
                i.append("अम्बा")
            elif i[0]=="Gourd":
                i.append("लौका")
            else:
                i.append(i[0])
    return render_to_response('agri/third.html', {'st': st})

def second (request):
            #return HttpResponse("Milan tori mula")
            template = loader.get_template('agri/second.html')
            context = {
                'a': "area",
            }
            return HttpResponse(template.render(context, request))

def map (request):
            #return HttpResponse("Milan tori mula")
            template = loader.get_template('agri/map.html')
            context = {
                'a': "area",
            }
            return HttpResponse(template.render(context, request))
