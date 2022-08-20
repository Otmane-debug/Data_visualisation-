from multiprocessing import context
from django.shortcuts import render
from .models import *
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from django.utils import timezone
from datetime import timedelta, date


def weekly(i, db):
    x_li = []    
    y_li = []


    date_object = date(2022, 1, 1)
    date_object = date_object + timedelta(days=-date_object.weekday(), weeks=1)

    while date_object <= timezone.now().date():
        x_li.append(date_object) 
        y_li.append(db.objects.filter(indicat=i).filter(date=str(date_object)).values()[0]['value'])

        date_object += timedelta(days=7)

    return x_li, y_li

def trimestrely(i, db):
    avg = []
    ss = []
        
    if db.objects.filter(indicat=i).filter(date__range=["2022-01-01", "2022-03-31"]):
        sum = 0
        le = len(db.objects.filter(indicat=i).filter(date__range=["2022-01-01", "2022-03-31"]))
            
        for v in db.objects.filter(indicat=i).filter(date__range=["2022-01-01", "2022-03-31"]):
            sum += v.value
            
        ss.append("S1")
        avg.append(round(sum/le, 3))
    else:
        print("date__range=[\"2022-01-01\", \"2022-03-31\"] :No Data Exist")
            
    if db.objects.filter(indicat=i).filter(date__range=["2022-04-01", "2022-06-30"]):
        sum = 0
        le = len(db.objects.filter(indicat=i).filter(date__range=["2022-04-01", "2022-06-30"]))
            
        for v in db.objects.filter(indicat=i).filter(date__range=["2022-04-01", "2022-06-30"]):
            sum += v.value
            
        ss.append("S2")
        avg.append(round(sum/le, 3))
    else:
        print("date__range=[\"2022-04-01\", \"2022-06-30\"] :No Data Exist")
            
    if db.objects.filter(indicat=i).filter(date__range=["2022-07-01", "2022-09-30"]):
        sum = 0
        le = len(db.objects.filter(indicat=i).filter(date__range=["2022-07-01", "2022-09-30"]))
            
        for v in db.objects.filter(indicat=i).filter(date__range=["2022-07-01", "2022-09-30"]):
            sum += v.value
            
        ss.append("S3")
        avg.append(round(sum/le, 3))
    else:
        print("date__range=[\"2022-07-01\", \"2022-09-30\"] :No Data Exist")
        
    if db.objects.filter(indicat=i).filter(date__range=["2022-10-01", "2022-12-31"]):
        sum = 0
        le = len(db.objects.filter(indicat=i).filter(date__range=["2022-10-01", "2022-12-31"]))
            
        for v in db.objects.filter(indicat=i).filter(date__range=["2022-10-01", "2022-12-31"]):
            sum += v.value

        ss.append("S4")
        avg.append(round(sum/le, 3))
    else:
        print("date__range=[\"2022-10-01\", \"2022-12-31\"] :No Data Exist")

    return avg, ss

def yearly(indi, db):
    avg_val = []
    mois_val = []
    
    for i in range(1, 13):
        if db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).exists() == False:
            break
        elif db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).exists():
            mois_val.append(str(i).zfill(2))        
    
    for i in range (1, 13):
        if db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).exists() == False:
            break
        elif db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).exists():
            sum = 0
            l = len(db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)))            
                
            for j in db.objects.filter(indicat=indi).filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)):
                sum += j.value
                    
            avg_tmp = sum / l
            avg_tmp = round(avg_tmp, 3)
                
            avg_val.append(avg_tmp)

    return avg_val, mois_val


def fusion(request):

    if request.method == "POST":
        v = []

        v.append(request.POST["value_1"])
        v.append(request.POST["value_2"])
        v.append(request.POST["value_3"])
        v.append(request.POST["value_4"])
        v.append(request.POST["value_5"])
        v.append(request.POST["value_6"])
        v.append(request.POST["value_7"])
        v.append(request.POST["value_8"])
        v.append(request.POST["value_9"])
        v.append(request.POST["value_10"])
        v.append(request.POST["value_11"])
        v.append(request.POST["value_12"])
        v.append(request.POST["value_13"])

        i = 0
        for e in KPI_secteur.objects.filter(secteur="Fusion").order_by('id'):
            e.data_set.create(value=v[i], date=date(2022, 12, 5)).save()
            i += 1


    return render(request, "main/forms/fusion.html", {})

def ccm(request):
    
    if request.method == "POST":
        v = []    

        v.append(request.POST["value_1"])
        v.append(request.POST["value_2"])
        v.append(request.POST["value_3"])
        v.append(request.POST["value_4"])
        v.append(request.POST["value_5"])
        v.append(request.POST["value_6"])
        v.append(request.POST["value_7"])
        v.append(request.POST["value_8"])
        v.append(request.POST["value_9"])
        v.append(request.POST["value_10"])


        i=0
        for e in KPI_secteur.objects.filter(secteur="CCM").order_by('id'):
            e.data_set.create(value=v[i], date=date(2022, 8, 22)).save()
            i += 1

        

    return render(request, "main/forms/ccm.html", {})


def auxilaire(request):
    if request.method == "POST":
        v = []    

        v.append(request.POST["value_1"])
        v.append(request.POST["value_2"])
        v.append(request.POST["value_3"])
        v.append(request.POST["value_4"])
        v.append(request.POST["value_5"])
        v.append(request.POST["value_6"])
        v.append(request.POST["value_7"])
        v.append(request.POST["value_8"])

        i=0
        for e in KPI_secteur.objects.filter(secteur="Auxiliaire").order_by('id'):
            e.data_set.create(value=v[i], date=date(2022, 9, 5)).save()
            i += 1


    return render(request, "main/forms/auxiliaire.html", {})


def index(request):
    return render(request, "main/index.html", {})

def fusion_graphs(request):
    plot_w = []

    
    for e in KPI_secteur.objects.filter(secteur="Fusion"):  
        x_l = []
        y_l = []
        
        x = KPI_secteur.objects.get(id=e.id)
        
        for d in  x.data_set.all().values():
            y_l.append(d['value'])
            x_l.append(d['date'])

        week = plot([Scatter(x=x_l, y=y_l, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
        plot_w.append(week)

    context = {
        "plot_w": plot_w, 
        }

    return render(request, 'main/graphs/fusion_g.html', context)

def ccn_graphs(request):

    return render(request, "main/graphs/ccn_g.html", {})

def auxiliaire_graphs(request):

    return render(request, 'main/graphs/auxiliaire_g.html', {})
