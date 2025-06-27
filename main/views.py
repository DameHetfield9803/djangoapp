from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
from .models import MenuItems, Reservation
# Create your views here.
def hello_world(req):
    return HttpResponse("Hello world")

class HelloBro(View):
    def get(self, req):
        return HttpResponse("Hello bro")
    

def form(req):
    form = ReservationForm()
    
    if(req.method == "POST"):
        form = ReservationForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'success.html', {'title':'Form successfully submitted'})
        else:
            return render(req, 'unsuccessful.html',{'title':'Form submitted unsuccessfully'})
    return render(req, 'form.html', {'form': form})

def landing(req):
    return render(req, 'landing.html', { 'title': "Welcome!" })

def menu(req):
    items = MenuItems.objects.all()
    return render(req, 'menu.html', {'title' : 'Menu items', 'items': items})

def showreservations(req):
    reservations = Reservation.objects.all()
    return render(req, 'reservations.html',{ 'title': 'All reservations', 'reservations': reservations })