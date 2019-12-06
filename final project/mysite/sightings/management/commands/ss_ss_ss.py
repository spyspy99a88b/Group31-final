#!/usr/bin/env python
import csv
from django.core.management import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('path')
       
    def handle(self,path,**options):
        with open(path,'rt') as fp:
            file = csv.DictReader(fp)
            reader=list(file)
            for row in reader:
                s = Squirrel(                  
                        latitude = row['Y'],
                        longitude = row['X'],                  
                        usi = row['Unique Squirrel ID'],
                        shift = row['Shift'],
                        date = row['Date'],
                        age = row['Age'],
                        pfc = row['Primary Fur Color'],
                        location = row['Location'],
                        sl = row['Specific Location'],
                        running = True if row['Running']=='TRUE' else False,
                        chasing = True if row['Chasing']=='TRUE' else False,
                        climbing = True if row['Climbing']=='TRUE' else False,
                        eating = True if row['Eating']=='TRUE' else False,
                        foraging = True if row['Foraging']=='TRUE' else False,
                        oa = row['Other Activities'],
                        kuks = True if row['Kuks'].lower()=='TRUE' else False,
                        quaas = True if row['Quaas'].lower()=='TRUE' else False,
                        moans = True if row['Moans'].lower()=='TRUE' else False,
                        tf = True if row['Tail flags'].lower()=='TRUE' else False,
                        tt = True if row['Tail twitches'].lower()=='TRUE' else False,
                        approaches = True if row['Approaches']=='TRUE' else False,
                        indifferent = True if row['Indifferent']=='TRUE' else False,
                        rf = True if row['Runs from'].lower()=='TRUE' else False,)
                s.save()
               

                    
                    
                

            