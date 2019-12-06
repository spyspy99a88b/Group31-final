#!/usr/bin/env python
import csv
from django.core.management import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):   
    def add_arguments(self, parser):
        parser.add_argument('path')
       
    def handle(self,path,**options):
        with open(path,'w') as fs:
            myWrite = csv.writer(fs)
            data = Squirrel.objects.all()
            myWrite.writerow(['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color',
                              'Location','Specific Location','Running','Chasing','Climbing','Eating',
                              'Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags',
                              'Tail twitches','Approaches','Indifferent','Runs from'])
            for s in data:
                myWrite.writerow([s.latitude,s.longitude,s.usi,s.shift,s.date,s.age,s.pfc,s.location,
                                  s.sl,s.running,s.chasing,s.climbing,s.eating,s.foraging,s.oa,s.kuks,
                                  s.quaas,s.moans,s.tf,s.tt,s.approaches,s.indifferent,s.rf])
        

               

                    
                    
                

            