from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()
    return render(request, 'resume_app/upload.html', {'form': form})

def dashboard(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_app/dashboard.html', {'resumes': resumes})