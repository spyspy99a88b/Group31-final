from django.db import models
    
class Squirrel(models.Model):
    latitude = models.DecimalField(max_digits=19,decimal_places=10)
    longitude = models.DecimalField(max_digits=19,decimal_places=10)
    usi = models.CharField(max_length=200,primary_key=True)  
    shift = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    age = models.CharField(max_length=200,blank=True)
    pfc = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200)
    sl = models.CharField(max_length=200)   
    running = models.BooleanField(blank=True,default=True)
    chasing = models.BooleanField(blank=True,default=True)
    climbing = models.BooleanField(blank=True,default=True)
    eating = models.BooleanField(blank=True,default=True)
    foraging = models.BooleanField(blank=True,default=True)
    oa = models.CharField(max_length = 200,blank=True)
    kuks = models.BooleanField(blank=True,default=True)
    quaas = models.BooleanField(blank=True,default=True)
    moans = models.BooleanField(blank=True,default=True)
    tf = models.BooleanField(blank=True,default=True)
    tt = models.BooleanField(blank=True,default=True)
    approaches = models.BooleanField(blank=True,default=True)
    indifferent = models.BooleanField(blank=True,default=True)
    rf = models.BooleanField(blank=True,default=True)


    