from django.shortcuts import redirect, render
from .forms import StudentForm

def home(request):
    return render(request, 'index.html')

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            return redirect('student_form')
    else:
        form = StudentForm 

    return render(request, 'form.html', {'form': form})
