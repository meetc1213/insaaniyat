from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request,'index.html',{'home_active':'active'})

# Create your views here.
