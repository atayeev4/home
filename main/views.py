from typing import Type
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import City, Apartment, UserApplication, Type
from .forms import UserData


def index(request):
    city = request.GET.get('city')
    type = request.GET.get('type')
    rooms = request.GET.get('rooms')

    apartments = Apartment.objects.all()

    if city:
        apartments = apartments.filter(city=city)
    if type:
        apartments = apartments.filter(type=type)
    if rooms:
        apartments = apartments.filter(rooms=rooms)

    apartments = Apartment.objects.order_by('-id')[:3].select_related('city')
    return render(request, 'main/index.html', {'apartments': apartments})


def apartments(request): 
    selectedCity = request.GET.get('city')
    selectedType = request.GET.get('type')
    selectedRooms = request.GET.get('rooms')

    apartments = Apartment.objects.order_by('-id').select_related('city')

    if selectedCity:
        apartments = apartments.filter(city=selectedCity)
    if selectedType:
        apartments = apartments.filter(type=selectedType)
    if selectedRooms:
        apartments = apartments.filter(rooms=selectedRooms)

    cities = City.objects.all()
    types = Type.objects.all()

    return render(request, 'main/apartments.html', {
        'apartments': apartments,
        'cities': cities,
        'types': types,
        'selectedType': selectedType,
        'selectedRooms': selectedRooms,
        'selectedCity': selectedCity,
    })


def post_application(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        name = data['name']
        phone = data['phone']
        description = data['description']
        form = UserApplication(name=name, phone=phone, description=description)
        form.save()
        return redirect('/')
    return redirect('/')

    
def detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    return render(request, 'main/detail.html', {
        'apartment': apartment
    })

