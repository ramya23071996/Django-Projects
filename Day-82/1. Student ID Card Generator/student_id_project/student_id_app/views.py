from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def upload_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'student_id_app/upload.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_id_app/list.html', {'students': students})