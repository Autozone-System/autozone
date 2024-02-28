from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from cms.resources.forms.vehicle import CreateVehicleForm





# def create(request):
#   if request.method == 'POST':
#     form = CreateMake(request)
#     data = form.clean()
#     vehicle = Vehicle.manager.create(data)
#     return redirect()
  
#   if request.method == 'GET':
#     form = CreateMake()
#     return render(request, 'vehicle/create.html', { 'form': form })
  
#   return Http404




def index(request):
  form = CreateVehicleForm()
  return render(request, 'pages/home.html', { "title" : "Autozone Dashboard", "form": form})




# def createMake(request, *args, **kwargs):
#   form = CreateMake(request.POST)
#   if form.is_valid():
#     make = form.save()
#     return redirect('make:detail', make.id)
#   return redirect('home')