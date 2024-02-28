from cms.resources.forms.make import CreateMake, UpdateMake
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, Http405
from common.models import Make


def create(request):
    if request.method == 'POST':
        form = CreateMake(request)
        form.clean()
        return redirect()
    
    
    if request.method == 'GET':
        form = CreateMake()
        return render(request, 'vehicle/create.html', { 'form': form })
    raise Http405
  
  

def update(request):
    if request.method == 'POST':
        form = CreateMake(request)
        form.clean()
        return redirect()
    
    
    if request.method == 'GET':
        form = CreateMake()
        return render(request, 'vehicle/create.html', { 'form': form })
    raise Http405