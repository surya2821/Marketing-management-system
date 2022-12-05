from django.contrib.auth import authenticate, login
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import  App

from django.contrib.auth.models import User
def home(response):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def admin(response):
    template=loader.get_template('admin.html')
    return HttpResponse(template.render())
def about(response):
    tempate4=loader.get_template('aboutus.html')
    return HttpResponse(tempate4.render())
def contact(response):
    template1=loader.get_template('contact.html')
    return HttpResponse(template1.render())
def online(response):
    template2=loader.get_template('online.html')
    return HttpResponse(template2.render())
def paper(response):
    template3=loader.get_template('paper.html')
    return HttpResponse(template3.render())
def payment(request):
    template5=loader.get_template('payment.html')
    return HttpResponse(template5.render())
def sdp(response):
    template6=loader.get_template('sdp.html')
    return HttpResponse(template6.render())
def service(response):
    template8=loader.get_template('service.html')
    return HttpResponse(template8.render())
def signup(request):
    template9=loader.get_template('signup.html')
    return HttpResponse(template9.render({},request))
def progress(response):
    template=loader.get_template('progress.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        x = request.POST['Fname']
        y = request.POST['lname']
        z = request.POST['email']
        b = request.POST['password']
        obj = App(Firstname=x,  lastname=y,  email=z,  password=b)
        obj.save()
        return HttpResponseRedirect(reverse('home'))
def payment2(request):
    template11=loader.get_template('payment2.html')
    return HttpResponse(template11.render())
def succesful(request):
    return HttpResponse("insert")
def table(request):
    members=App.objects.all().values()
    template=loader.get_template('table.html')
    context={'members':members}
    return HttpResponse(template.render(context,request))
def branches(request):
    template12=loader.get_template('branches.html')
    return HttpResponse(template12.render())

