from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Car:
    def __init__(self, model, make, description, milage):
        self.model = model
        self.make = make
        self.description = description
        self.milage = milage

cars = [
    Car('Camaro', 'Chevy', 'Lorem ipsum do.', 20000),
    Car('Mustang', 'Ford', 'Lorem ipsum do.', 35000),
    Car('400z', 'Nissan', 'Lorem ipsum do.', 12000),
]

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})