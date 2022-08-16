from django.db import models


class Fusion(models.Model):
    indicat = models.CharField(max_length=200)
    date = models.DateField()
    value = models.IntegerField()
    
    def __str__(self):
        return str(self.value)

class Ccn(models.Model):
    indicat = models.CharField(max_length=200)
    date = models.DateField()
    value = models.IntegerField()
    
    def __str__(self):
        return str(self.value)

class Auxiliaire(models.Model):
    indicat = models.CharField(max_length=200)
    date = models.DateField()
    value = models.IntegerField()
    
    def __str__(self):
        return str(self.value)