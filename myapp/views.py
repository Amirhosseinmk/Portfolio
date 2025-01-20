from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import users,projects,languages,assign_language
# Create your views here.

def home(request):
    return render(request,'home.html')

def navbar(request):
    return render(request,'navbar.html')

def Project(request):
    all_projects = projects.objects.all()
    context = {'projects':all_projects}
    return render(request,'projects.html',context)

def education_chem(request):
    return render(request,'chem.html')

def software_eng(request):
    return render(request,'software.html')
    

