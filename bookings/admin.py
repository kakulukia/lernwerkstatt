from django.contrib import admin
from .models import TimeSlot, Booking


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start', 'end']
    actions = None


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['start', 'name', 'group_size', 'accepted']
    list_filter = ['accepted', 'start']
    actions = None
