from django.shortcuts import render
from login_app.models import deatils
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def sgin_up(request):
    if request.method=="POST":
        fname=request.POST.get('first')
        lname=request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('password')
        deatils.objects.create(first_name=fname,last_name=lname,email=email,password=password)
        d={"name":fname+" "+lname+"is successfully added"}
        send_mail('thank you for regtration  your login details',f"user:{fname} and your password {password}",'settings.EMAIL_HOST_USER',[email],fail_silently=False)
        return render(request,'sign.html',d)

    return render(request,'sign.html')

def sgin_in(request):
     if request.method=="POST":
        fname=request.POST.get('first')
        passwords=request.POST.get('password')
        search=deatils.objects.get(first_name=fname)
        if search.password==passwords:
            return render(request,'main.html')
        else:
            return render(request,'sign.html',{"message":"enter login details is worng"})


