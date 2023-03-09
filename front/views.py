from django.shortcuts import render, redirect
from django.http import HttpResponse
from shipments.models import Shipment
from django.urls import reverse

def index(request):
    if request.method == "POST":
        print(request.POST)
        shipment_id = request.POST.get("shipment_id")
        return redirect(reverse("track_shipment", kwargs={"shipmentId":shipment_id}))
    return render(request, "index.html", {"showSlider":True})



def services(request):
    return render(request, "services.html")




def about_us(request):
    return render(request, "about_us.html")


def contact_us(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")



def register(request):
    return render(request, "register.html")





def track_shipment(request, shipmentId):
    shipment = Shipment.objects.filter(uuid=shipmentId)
    if not shipment.exists():
        return HttpResponse("Shipment with this UUID does not exist")
    shipment = shipment[0]
    return render(request, 'track_shipment.html', {"shipment":shipment})
    

def print_invoice(request, shipmentId):
    shipment = Shipment.objects.filter(uuid=shipmentId)
    if not shipment.exists():
        return HttpResponse("Shipment with this UUID does not exist")
    shipment = shipment[0]
    return render(request, 'print_invoice.html', {"shipment":shipment})