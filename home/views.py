from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.conf import settings
from django.http import HttpResponse
from home.models import donors
from home.models import recipient
from datetime import datetime
def home(request):
    return render(request,'index.html',{'home_active':'active'})
def donor_form(request):
    if request.method=='POST':
        print(request.POST)
        record=donors(
            name = request.POST.get('first_name')+" "+request.POST.get('last_name'),
            gender= request.POST.get('gender'),
            bloodgroup= request.POST.get('bloodgrp'),
            date_pos=datetime.strptime(request.POST.get('pos_test'), "%Y-%m-%d").strftime("%d/%m/%Y"),
            date_neg=datetime.strptime(request.POST.get('neg_test'), "%Y-%m-%d").strftime("%d/%m/%Y"),
            email= request.POST.get('email'),
            phone= request.POST.get('phone'),
            city= request.POST.get('city'),
            exist_cond= request.POST.get('pre-cond'),

        )
        record.save()
    return render(request,'donor_form.html',{})
def recipient_form(request):
    if request.method=='POST':
        print(request.POST)
        record=recipient(
            name = request.POST.get('first_name')+" "+request.POST.get('last_name'),
            gender= request.POST.get('gender'),
            bloodgroup= request.POST.get('bloodgrp'),
            hospital= request.POST.get('hospital'),
            amt_needed= request.POST.get('amt'),
            email= request.POST.get('email'),
            phone= request.POST.get('phone'),
            city= request.POST.get('city'),
            exist_cond= request.POST.get('pre-cond'),

        )
        record.save()
    return render(request,'recipient_form.html',{})
# Create your views here.
