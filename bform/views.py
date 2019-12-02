from django.shortcuts import render
from django.http import HttpResponse
from .forms import HostsForm,VisitorsForm,VisitorsOutForm
import json
import requests
from json import loads
from django.utils import timezone
from .models import Hosts,Visitors
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return HttpResponse("<h1>MyClub Event Calendar</h1>")

def host_new(request):
    if request.method == "POST":
        form=HostsForm(request.POST)
        if form.is_valid():
            host = form.save(commit=False)
            host.save()
            return render_to_response('bform/return_s.html')
        else:
            return render_to_response('bform/return_u.html')
    else:
        form=HostsForm()
    return render(request,'bform/host_edit.html',{'form':form})

def visitor_new(request):
    if request.method == "POST":
        form=VisitorsForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.save()
            n_visitor=Visitors.objects.get(phone=request.POST['phone'])
            r_host = Hosts.objects.get(id=n_visitor.name_of_host_id_id)
            subject = 'Meeting member arrived'
            message = 'This person arrived at meeting\nName:'+request.POST['name']+'\nEmail:'+request.POST['email']+'\nPhone:'+request.POST['phone']+'\nCheckin Time:'+str(timezone.now())
            email_from=settings.EMAIL_HOST_USER
            recipient_list= [r_host.email,]
            send_mail( subject, message, email_from, recipient_list )
            url = "https://www.fast2sms.com/dev/bulk"
            payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+str(r_host.phone)
            headers = {
                'authorization': "yourFAST2SMSAPI",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            return render_to_response('bform/return_s.html')
        else:
            return render_to_response('bform/return_u.html')

    else:
        form=VisitorsForm()
    return render(request,'bform/visitor_edit.html',{'form':form})

def visitor_out(request):
    if request.method == "POST":
        Visitors.objects.filter(phone=request.POST['phone']).update(check_out_v=timezone.now())
        n_visitor=Visitors.objects.get(phone=request.POST['phone'])
        r_host = Hosts.objects.get(id=n_visitor.name_of_host_id_id)
        subject ='Thank you for your visit at Innovaccer'
        message='Name:'+n_visitor.name+'\nPhone:'+str(n_visitor.phone)+'\nCheck-in time:'+str(n_visitor.check_in)+'\nCheck-out time:'+str(n_visitor.check_out_v)+'\nHost name:'+r_host.name
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [n_visitor.email,]
        send_mail(subject,message,email_from,recipient_list)
        form=VisitorsOutForm()
        return render_to_response('bform/return_s.html')
    else:
        form=VisitorsOutForm()
    return render(request,'bform/visitor_out.html',{'form':form})