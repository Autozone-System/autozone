from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from cms.resources.forms.vehicle import CreateVehicleForm
from common.models import Vehicle





# def get(request, id):
#     vehicle = get_object_or_404(Vehicle, id=id)
#     return render(request, 'pages/vehicle/detail.html', { 'vehicle': vehicle })


def create(request):
    if request.method == 'POST':
        form = CreateVehicleForm(request.POST)
        vehicle = Vehicle.manager.create(form.clean())
        return redirect('vehicle-detail', vehicle.id)
    if request.method == 'GET':
        form = CreateVehicleForm()
        return render(request, 'pages/vehicle/index.html', { 'form': form })
    # return Http404