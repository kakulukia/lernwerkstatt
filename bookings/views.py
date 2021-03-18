from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from bookings.forms import BookingForm
from bookings.models import Page


def index(request):
    return render(request, "index.pug")


def show_page(request, name):
    page = get_object_or_404(Page, url=name)
    return render(request, "page.pug", {'page': page})


class BookingView(FormView):
    template_name = 'booking.pug'
    form_class = BookingForm
    success_url = '/danke'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form)
