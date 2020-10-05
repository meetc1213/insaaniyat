from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.conf import settings
from django.http import HttpResponse
def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)
def home(request):
    return render(request,'home.html',{'home_active':'active'})
def aboutus(request):
    return render(request,'aboutus.html',{'team_active':'active'})
def drives(request):
    return render(request,'drives.html',{'drives_active':'active'})
def contactus(request):
    diction={'contact_active':'active'}
    if request.method=='POST':
        mail1=('Enquiry- Route India',"Hello "+request.POST['name_contact']+" "+request.POST['lastname_contact']+",\n\nThank you for contacting us! We have received your message and you will be shortly contacted by us.\n\nRegards,\n\nTeam Route\nRoute for a better India!",settings.EMAIL_HOST_USER,[request.POST['email_contact']])
        mail2=('Enquiry submitted',"Alert!\n\nAn enquiry has been submitted by "+request.POST['name_contact']+" "+request.POST['lastname_contact']+".\nHis/her email is '"+request.POST['email_contact']+ "' and phone number is "+request.POST['phone_contact'] +"\nThe message sent is as follows:-\n'"+request.POST['message_contact']+"'",settings.EMAIL_HOST_USER,['route.india.team@gmail.com','mdc8464@gmail.com','vishnusojitra7@gmail.com'])
        try:
            send_mass_mail((mail1,mail2),fail_silently=False,)
        except:
            diction['mail_err']='ERROR: Kindly use our email route.india.team@gmail.com to reach us.'
    return render(request,'contactus.html',context=diction)
# Create your views here.
