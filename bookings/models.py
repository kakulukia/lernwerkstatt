from django.db import models
from django_undeletable.models import BaseModel


class TimeSlot(BaseModel):
    start = models.TimeField(verbose_name="Start")
    end = models.TimeField(verbose_name="Ende")

    class Meta(BaseModel.Meta):
        verbose_name = "Zeitslot"
        verbose_name_plural = "Zeitslots"


class Booking(BaseModel):
    accepted = models.BooleanField(verbose_name="bestätigt")

    start = models.DateTimeField(verbose_name="Start")

    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="E-Mail-Adresse")
    group_size = models.IntegerField(verbose_name="Gruppengröße")

    class Meta(BaseModel.Meta):
        verbose_name = "Buchung"
        verbose_name_plural = "Buchungen"
