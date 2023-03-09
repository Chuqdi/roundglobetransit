
from django.contrib import admin
from django.urls import path
from front.views import index, login, print_invoice, register,about_us, contact_us, services,track_shipment




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("about_us", about_us, name="about_us"),
    path("contact_us", contact_us, name="contact_us"),
    path("services", services, name="services"),
    path("trackShipment/<shipmentId>/", track_shipment, name="track_shipment"),
    path("print_invoice/<shipmentId>/", print_invoice, name="print_invoice")

]
