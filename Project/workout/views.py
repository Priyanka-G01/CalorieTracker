from django.shortcuts import render
from .models import Workout, CaloriesLostInDay
from bmi.models import Bmi
# Create your views here.

def workout(request):
    context = {}
    if request.method == "POST":
        wrkout = request.POST.get('workout-details') 
        lost = Workout.objects.get(name = wrkout)
        weight = float(request.POST.get('weight'))
        duration = float(request.POST.get('duration'))
        
        total = (duration*(lost.met * 3.5 * weight))/200
        save = request.POST.get("save")
        workouts = Workout.objects.all()
        bmis = Bmi.objects.all()
        if save == "on":
            CaloriesLostInDay.objects.create(name = lost, weight = weight, duration = duration, total= total)
    
        context['total'] = total
        context['workouts'] = workouts
        #context['bmis'] = bmis
    else:
        workouts = Workout.objects.all()
        bmis = Bmi.objects.all()
        context['workouts'] = workouts
        #context['bmis'] = bmis
    return render(request, 'workout/workout.html',context)