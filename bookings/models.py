from django.db import models
from django.template.defaultfilters import date
from django_undeletable.models import BaseModel
from django_quill.fields import QuillField


class TimeSlot(BaseModel):
    start = models.TimeField(verbose_name="Start")
    end = models.TimeField(verbose_name="Ende")

    class Meta(BaseModel.Meta):
        verbose_name = "Zeitraum"
        verbose_name_plural = "Zeiträume"
        ordering = ['start']

    def __str__(self):
        return f'{date(self.start, "H:i")} - {date(self.end, "H:i")}'


class Booking(BaseModel):
    class Status(models.TextChoices):
        NEW = 'new', 'neu'
        ACCEPTED = 'accepted', 'bestätigt'
        REJECTED = 'rejected', 'abgelehnt'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.NEW,
    )

    start = models.DateTimeField(verbose_name="Datum")
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, null=True, verbose_name="Zeitraum")

    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="E-Mail-Adresse")
    group_size = models.IntegerField(verbose_name="Gruppengröße")

    class Meta(BaseModel.Meta):
        verbose_name = "Buchung"
        verbose_name_plural = "Buchungen"


class Page(BaseModel):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=20)

    text = QuillField()

    class Meta(BaseModel.Meta):
        verbose_name = "Seite"
        verbose_name_plural = "Seiten"
