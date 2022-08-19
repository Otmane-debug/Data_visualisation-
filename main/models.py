from django.db import models



class KPI_secteur(models.Model):
    site = models.CharField(max_length=300)
    unite = models.CharField(max_length=300)
    secteur = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    indicateur_perfor = models.CharField(max_length=300)

    def __str__(self):
        return self.indicateur_perfor
    

class Data(models.Model):
    indicateur = models.ForeignKey(KPI_secteur, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return str(self.value)