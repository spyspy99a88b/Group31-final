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
                        date = row['Date'][4:]+'-'+row['Date'][:2]+'-'+row['Date'][2:4],
                        age = row['Age'],
                        pfc = row['Primary Fur Color'],
                        location = row['Location'],
                        sl = row['Specific Location'],
                        running = True if row['Running'].lower()=='true' else False,
                        chasing = True if row['Chasing'].lower()=='true' else False,
                        climbing = True if row['Climbing'].lower()=='true' else False,
                        eating = True if row['Eating'].lower()=='true' else False,
                        foraging = True if row['Foraging'].lower()=='true' else False,
                        oa = row['Other Activities'],
                        kuks = True if row['Kuks'].lower()=='true' else False,
                        quaas = True if row['Quaas'].lower()=='true' else False,
                        moans = True if row['Moans'].lower()=='true' else False,
                        tf = True if row['Tail flags'].lower()=='true' else False,
                        tt = True if row['Tail twitches'].lower()=='true' else False,
                        approaches = True if row['Approaches'].lower()=='true' else False,
                        indifferent = True if row['Indifferent'].lower()=='true' else False,
                        rf = True if row['Runs from'].lower()=='true' else False,)
                s.save()
               

                    
                    
                

            