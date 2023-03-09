from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save

from utils.randomString import GenerateRandomString


class Reciever(models.Model):
    full_name = models.CharField(null=False, blank=False, max_length=120)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(null=False, blank=False, max_length=120)
    location = models.CharField(null=False, blank=False,max_length=120)

    def __str__(self) -> str:
        return self.email

    

    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateReciever", kwargs={"pk":self.pk})


class Sender(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    full_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length =30,null=False)
    


    def __str__(self) -> str:
        return self.full_name



class Deliverer(models.Model):
    deliverer_name = models.CharField(max_length=510)


    def __str__(self) -> str:
        return self.deliverer_name


    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateDeliverer",kwargs={"pk":self.pk})




class Payment(models.Model):
    clearance_debt = models.IntegerField(null=True, blank=True)
    recovery_debt = models.IntegerField(null=True, blank=True)
    agency_debt = models.IntegerField(null=True, blank=True)
    requirements_and_neccessities = models.IntegerField(null=True, blank=True)
    auxillaries = models.IntegerField(null=True, blank=True)





    def __str__(self) -> str:
        return str(self.clearance_debt)

    

    @property
    def get_payment_total(self):
        total =0
        
        
        return int(int(self.clearance_debt) + int(self.recovery_debt) + int(self.agency_debt) + int(self.requirements_and_neccessities) +int(self.auxillaries))+20.01



class Location(models.Model):
    current_location = models.CharField(null=False, blank=False, max_length=120)
   


    class Meta:
        ordering=("-id",)



    def get_absolute_url(self, *args, **kwargs):
        return reverse("updateLocation", kwargs={"pk":self.pk})



    def __str__(self) -> str:
        return self.current_location

class Shipment(models.Model):
    weight = models.CharField(null=True, blank=True, max_length=120)
    quantity = models.CharField(null=True, blank=True, max_length=120)
    mode_of_shipment = models.CharField(null=True, blank=True, max_length=120)
    shipment_pick_up_date = models.CharField(null=True, blank=True, max_length=120)
    shipment_type = models.CharField(null=True, blank=True, max_length=120)
    comment = models.CharField(null=True, blank=True, max_length=120)
    uuid = models.TextField(null=True, blank=True, unique=True)
    destination = models.CharField(null=True, blank=True, max_length=120)
    date_created = models.DateTimeField(default=timezone.now)
    registered_by = models.CharField(max_length=60, null=True, blank=True)

    reciever = models.ForeignKey(Reciever, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    payments = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True, blank=True)


    is_paid = models.BooleanField(default=False)
    is_arrived = models.BooleanField(default=False)



    def get_absolute_url(self):
        return reverse("updateShipment", kwargs={"pk": self.id})
    




    def __str__(self) -> str:
        return self.uuid




def assignUdid(instance):
    if  len(instance.uuid) < 1:
        uuid = GenerateRandomString.randomStringGenerator(7)
        try:
            Shipment.objects.get(uuid=uuid)
            assignUdid(instance)
        except:
            instance.uuid = uuid

def shipmentUuid(sender, instance, *args,**kwargs):
    assignUdid(instance)
    


pre_save.connect(shipmentUuid, sender=Shipment)