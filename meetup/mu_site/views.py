from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, "mu_site\index.html", {
        "meetups": meetups
    })

def meetup_detail(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    if request.method == "GET":        
        registration_form = RegistrationForm()
    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data["email"]
            participant, _ = Participant.objects.get_or_create(email=user_email)
            meetup.participant.add(participant)
            return redirect("reg_confirmation", meetup_slug=slug)

    return render(request, "mu_site\meetup-detail.html", {
            "meetup": meetup,
            "reg_form": registration_form
        })

def confirm_registration(request, meetup_slug):
    return render(request, "mu_site/registration-succes.html")