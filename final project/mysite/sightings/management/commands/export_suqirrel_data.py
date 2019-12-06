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
            data = Squirrel.object.all()
            myWrite.writerow(['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            for s in data:
                myWrite.writerow([s.latitude])
        
               

                    
                    
                

            