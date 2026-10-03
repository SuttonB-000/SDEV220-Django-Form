from django.shortcuts import render
from .forms import StudentForm

def home(request):
    return render(request, 'index.html')

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            student_id = form.cleaned_data['student_id']
            major = form.cleaned_data['major']
            class_standing = form.cleaned_data['class_standing']
            programming_languages = form.cleaned_data['programming_languages']
            graduation_year = form.cleaned_data['graduation_year']
            comments = form.cleaned_data['comments']

            return render(request, 'form.html',{
                'form': form,
                'submitted': True,
                'student_name': student_name,
                'student_id': student_id,
                'major': major,
                'class_standing': class_standing,
                'programming_languages': programming_languages,
                'graduation_year': graduation_year,
                'comments': comments,
            })
    else:
        form = StudentForm() 

    return render(request, 'form.html', {'form': form})
