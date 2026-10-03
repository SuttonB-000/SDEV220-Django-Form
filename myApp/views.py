from django.shortcuts import render
from .forms import StudentForm

def home(request):
    return render(request, 'myApp/index.html')

def student_form(request):
    # student form logic
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student_name = form.cleaned_data["studnet_name"]
            student_id = form.cleaned_data["student_id"]
            major = form.cleaned_data['major']
            class_standing = form.cleaned_data['class_standing']
            programming_languages = form.cleaned_data['programming_languages']
            graduation_year = form.cleaned_data['graduation_year']

        else:
            form = StudentForm()

        return render(request, 'student_form.html', {'form':form})
