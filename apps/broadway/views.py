from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

def home(request):
    return render(request, "broadway/home.html")
    
def menu(request):
    return render(request, "broadway/menu.html")

def hours(request):
    return render(request, "broadway/hours.html")

