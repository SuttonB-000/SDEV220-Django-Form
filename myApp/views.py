from django.shortcuts import render
from .forms import StudentForm

def home(request):
    return render(request, 'home.html')
