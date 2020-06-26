# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import form_submission

def index(request):
	return render(request, "ytsite/playlist.html")

def about(request):
    return render(request, "ytsite/about.html")


def create_form(request):
	return render(request, "ytsite/upload.html")
# Create your views here. 
def created(request):
    if request.method == "POST" :
        form = form_submission()
        form.playlist = request.POST.get('playlist')
        form.card_name = request.POST.get('card_name')
        form.card_text = request.POST.get('card_details')
        form.photo = request.FILES['image']
        form.url = request.POST.get('link')
        form.save()
        usr = form_submission.objects.all()
        return render(request, "ytsite/created.html", {'usr' : usr})


def nodata(request):
    return render(request, "ytsite/nodata.html")


#playlist starts here
def solidworks(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/solidworks.html", {'usr' : usr})

def needhelp(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/needhelp.html", {'usr' : usr})

def ors(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/ors.html", {'usr' : usr})

def tech(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/tech.html", {'usr' : usr})

def gci(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/gci.html", {'usr' : usr})

def slomo(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/slomo.html", {'usr' : usr})

def methermo(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/methermo.html", {'usr' : usr})

def gatecs(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/gatecs.html", {'usr' : usr})

def memechanical(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/memechanical.html", {'usr' : usr})

def som(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/som.html", {'usr' : usr})

def bloging(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/bloging.html", {'usr' : usr})

def python(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/python.html", {'usr' : usr})