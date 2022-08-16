from django.shortcuts import render
from .models import Fusion, Auxiliaire, Ccn
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
        if db.objects.filter(indicat=i).filter(date=str(date_object)).values().exists() == False:
            print("Pas de valeur dans la semaine " + str(date_object))
        else:
            x_li.append(date_object) 

        if db.objects.filter(indicat=i).filter(date=str(date_object)).exists() == False:
            print("No value in " + str(date_object))
        else:
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
    x_li = []
    y_li = []
    avg = []
    ss = []
    avg_val = []
    mois_val = []
    titre = ""

    if request.method == "POST":
        va = request.POST.get("value", False)
        da = request.POST.get("date", False)    
        ind = request.POST.get("indicateur", False)

        if Fusion.objects.filter(indicat=ind).filter(date=da).exists():
            print("value exists !")
        else:
            Fusion(value = va, date=da, indicat=ind).save()

        x_li, y_li = weekly(ind, Fusion)
        avg, ss = trimestrely(ind, Fusion)
        avg_val, mois_val = yearly(ind, Fusion)
        
        titre = ind

    plot_mondays_div = plot([Scatter(x=x_li, y=y_li, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    plot_trimester_div = plot([Scatter(x=ss, y=avg, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    plot_year_div = plot([Scatter(x=mois_val, y=avg_val, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")

    context = {
        "plot_mondays_div": plot_mondays_div,
        "plot_trimester_div": plot_trimester_div,
        "plot_year_div": plot_year_div,
        "titre": titre,
    }

    return render(request, "main/fusion.html", context)

def ccm(request):
    x_li = []
    y_li = []
    avg = []
    ss = []
    avg_val = []
    mois_val = []
    titre = ""

    if request.method == "POST":
        va = request.POST.get("value", False)
        da = request.POST.get("date", False)    
        ind = request.POST.get("indicateur", False)

        if Ccn.objects.filter(indicat=ind).filter(date=da).exists():
            print("value exists !")
        else:
            Ccn(value = va, date=da, indicat=ind).save()

        x_li, y_li = weekly(ind, Ccn)
        avg, ss = trimestrely(ind, Ccn)
        avg_val, mois_val = yearly(ind, Ccn)
        
        titre = ind

    plot_mondays_div = plot([Scatter(x=x_li, y=y_li, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    plot_trimester_div = plot([Scatter(x=ss, y=avg, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    plot_year_div = plot([Scatter(x=mois_val, y=avg_val, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")

    context = {
        "plot_mondays_div": plot_mondays_div,
        "plot_trimester_div": plot_trimester_div,
        "plot_year_div": plot_year_div,
        "titre": titre,
    }

    return render(request, "main/ccm.html", context)


def index(request):
    return render(request, "main/index.html", {})