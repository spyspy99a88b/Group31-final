from .models import Squirrel
from django.db.models import Max,Count,Min
from .forms import SquirrelForm
from django.shortcuts import render,redirect

def list(request):
    sightings = Squirrel.objects.all()[:125]
    return render(request,'sightings/list.html',{'sightings':sightings})

def stats(request):
    data = Squirrel.objects.all()
    longitude_m = data.aggregate(longitude_max = Max('longitude'))
    latitude_m = data.aggregate(latitude_min = Min('latitude'))
    date_m = data.aggregate(date_max = Max('date'))
    pfc_c = data.values('pfc').annotate(Count('pfc')).distinct()
    age_c=data.values('age').annotate(Count('age')).distinct()
    
    s={"longitude_m":longitude_m,"latitude_m":latitude_m,
       "age_c":age_c, "date_m":date_m,"pfc_c":pfc_c}    
    return render(request, 'sightings/stats.html',s)

def add(request):
    if request.method == 'POST':       
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form =SquirrelForm()

    context = {
        'form': form,
        'jazz': True,
    }

    return render(request,'sightings/update.html', context)

def update(request,idd):
    squ=Squirrel.objects.get(usi=idd)
    if request.method == 'POST':
        form=SquirrelForm(request.POST,instance=squ)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form=SquirrelForm(instance=squ)
    context={'form': form,}
    return render(request,'sightings/update.html',context)





        
