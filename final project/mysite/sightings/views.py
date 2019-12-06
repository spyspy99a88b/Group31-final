from django.shortcuts import render,redirect
from .models import Squirrel
from django.http import HttpResponse
from django.db.models import Max,Count
from .forms import SquirrelForm

def list(request):
    sightings = Squirrel.objects.all()[:125]
    return render(request,'sightings/list.html',{'sightings':sightings})

def delete(request,idd):
    obj_d= Squirrel.objects.filter(usi=idd)
    obj_d.delete()
 #return redirect(reverse('sightings:list'))

def stats(request):
    data = Squirrel.objects.all()
    longitude_m = data.aggregate(longitude_min = Max('longitude'))
    latitude_m = data.aggregate(latitude_min = Max('latitude'))
    age_m = data.aggregate(age_min = Max('age'))
    date_m = data.aggregate(date_min = Max('age'))
    color_c = data.values_list('pfc').annotate(Count('pfc'))  
    s={"longitude_m":longitude_m,"latitude_m":latitude_m,
       "age_m":age_m, "date_m":date_m,"color_c":color_c}
    return render(request, 'sightings/stats.html',s)

def add(request):
    return HttpResponse("nothing!")


def update(request,idd):
    squ=Squirrel.objects.get(usi=idd)
    if request.method == 'POST':
        form=SquirrelFrom(request.POST,instance=squ)
        if form.is_valid():
            form.save()
            return redirect('sightings/list.html')
    else:
        form=SquirrelForm(instance=squ)
    context={'form': form,}
    return render(request,'sightings/update.html',context)




# def edit_pet(request, pet_id):
#     pet = Pet.objects.get(id=pet_id)
#     if request.method == 'POST':
#         form = PetFrom(request.POST, instance=pet)
        
#         if form.is_valid():
#             form.save()
#             return redirect(f'/adpot/{pet_id}')
#     else:
#         form = PetForm(instance=pet)
#     context = {'form': form,}
#     return render(request, 'adopt/edit.html', context)





    
    

