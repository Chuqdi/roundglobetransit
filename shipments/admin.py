from django.contrib import admin
from .models import Shipment, Reciever, Deliverer,Location,Sender, Payment


admin.site.register(Location)
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_filter =["uuid"]
admin.site.register(Reciever)
admin.site.register(Deliverer)
admin.site.register(Sender)
admin.site.register(Payment)




