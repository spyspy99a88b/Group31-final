#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import csv
from django.core.management import BaseCommand
from sightings.models import squirrel

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                if row[0]!='X':
                    data = squirrel.objects.create(                  
                        latitude = row[1],
                        longitude = row[0],                  
                        USI = row[2],
                        Shift = row[4],
                        Date = row[5],
                        Age = row[7],
                        PFC = row[8],
                        Location = row[12],
                        SL = row[14],
                        Running = row[15])
                    
#                     Chasing = 
#                     Climbing = 
#                     Eating = 
#                     Foraging =  
#                     OA = 
#                     Kuks =   
#                     Quaas = 
#                     Moans =    
#                     TF =   
#                     TT =   
#                     Approaches = 
#                     Indifferent = 
#                     Runs =    
                    
                    
                    
                

            