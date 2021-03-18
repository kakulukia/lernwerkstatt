from django.contrib import admin
from .models import TimeSlot, Booking, Page


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start', 'end']
    actions = None


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['start', 'name', 'group_size', 'status']
    list_filter = ['status', 'start']
    actions = None


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name']
