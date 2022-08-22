from multiprocessing import context
from django.shortcuts import render
from .models import *
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from django.utils import timezone
from datetime import timedelta, date


def weekly(i, db):

    plots = []
    
    for e in db.objects.filter(secteur=i):  
        x_l = []
        y_l = []
    
        x = db.objects.get(id=e.id)
        
        for d in  x.data_set.all().values():
            y_l.append(d['value'])
            x_l.append(d['date'])

        week = plot([Scatter(x=x_l, y=y_l, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
        plots.append(week)

    return plots

def trimestrely(i, db):
    plots = []
    
    
    for e in db.objects.filter(secteur=i):  
        x_l = []
        y_l = []        
        x = db.objects.get(id=e.id)

        if x.data_set.filter(date__range=["2022-01-01", "2022-03-31"]).values():
            sum = 0
            l = len(x.data_set.filter(date__range=["2022-01-01", "2022-03-31"]).values())
            for d in  x.data_set.filter(date__range=["2022-01-01", "2022-03-31"]).values():
                sum += d['value']

            y_l.append(round(sum/l, 3))
            x_l.append("S1")
        else:
            print('no data')

        if x.data_set.filter(date__range=["2022-04-01", "2022-06-30"]).values():
            sum = 0
            l = len(x.data_set.filter(date__range=["2022-04-01", "2022-06-30"]).values())
            for d in  x.data_set.filter(date__range=["2022-04-01", "2022-06-30"]).values():
                sum += d['value']

            y_l.append(round(sum/l, 3))
            x_l.append("S2")
        else:
            print('no data')

        if x.data_set.filter(date__range=["2022-07-01", "2022-09-30"]).values():
            sum = 0
            l = len(x.data_set.filter(date__range=["2022-07-01", "2022-09-30"]).values())
            for d in  x.data_set.filter(date__range=["2022-07-01", "2022-09-30"]).values():
                sum += d['value']

            y_l.append(round(sum/l, 3))
            x_l.append("S3")
        else:
            print('no data')

        sum = 0

        if x.data_set.filter(date__range=["2022-10-01", "2022-12-31"]).values():
            l = len(x.data_set.filter(date__range=["2022-10-01", "2022-12-31"]).values())
            for d in  x.data_set.filter(date__range=["2022-10-01", "2022-12-31"]).values():
                sum += d['value']

            y_l.append(round(sum/l, 3))
            x_l.append("S4")
        else:
            print('no data')

        tri = plot([Scatter(x=x_l, y=y_l, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
        plots.append(tri)

    return plots

def yearly(indi, db):
    
    plots = []
    
    for e in KPI_secteur.objects.filter(secteur="Fusion"):
        x_l = []
        y_l = []

        for i in range (1, 13):
            sum = 0
            if e.data_set.filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).exists() == False:
                print("no data")
                continue
            else:
                l = len(e.data_set.filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)))
                for ee in e.data_set.filter(date__startswith=str(timezone.now().year) + "-" +str(i).zfill(2)).values():
                   sum += ee['value']
                
                y_l.append(round(sum/l, 3))
                x_l.append(str(i).zfill(2))


        year = plot([Scatter(x=x_l, y=y_l, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
        plots.append(year)
    
    return plots


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
    nom = []
    plot_w = []
    plot_tri = []
    plot_y = []

    for e in KPI_secteur.objects.filter(secteur="Fusion"):  
        nom.append(e.indicateur_perfor)

    plot_w = weekly("Fusion", KPI_secteur)
    plot_tri = trimestrely("Fusion", KPI_secteur)
    plot_y = yearly("Fusion", KPI_secteur)

    context = {
        "nom": nom,
        "plot_w": plot_w,
        "plot_tri": plot_tri,
        "plot_y": plot_y, 
        }

    return render(request, 'main/graphs/fusion_g.html', context)

def ccm_graphs(request):
    nom = []
    plot_w = []
    plot_tri = []
    plot_y = []

    for e in KPI_secteur.objects.filter(secteur="CCM"):  
        nom.append(e.indicateur_perfor)

    plot_w = weekly("CCM", KPI_secteur)
    plot_tri = trimestrely("CCM", KPI_secteur)
    plot_y = yearly("CCM", KPI_secteur)

    context = {
        "nom": nom,
        "plot_w": plot_w,
        "plot_tri": plot_tri,
        "plot_y": plot_y, 
        }

    return render(request, "main/graphs/ccm_g.html", context)

def auxiliaire_graphs(request):
    nom = []
    plot_w = []
    plot_tri = []
    plot_y = []

    for e in KPI_secteur.objects.filter(secteur="Auxiliaire"):  
        nom.append(e.indicateur_perfor)

    plot_w = weekly("Auxiliaire", KPI_secteur)
    plot_tri = trimestrely("Auxiliaire", KPI_secteur)
    plot_y = yearly("Auxiliaire", KPI_secteur)

    context = {
        "nom": nom,
        "plot_w": plot_w,
        "plot_tri": plot_tri,
        "plot_y": plot_y, 
        }

    return render(request, 'main/graphs/auxiliaire_g.html', context)
