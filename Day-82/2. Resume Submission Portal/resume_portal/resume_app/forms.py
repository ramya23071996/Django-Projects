from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def clean_resume_file(self):
        file = self.cleaned_data.get('resume_file')
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            if file.size > 2 * 1024 * 1024:
                raise forms.ValidationError("File size must be under 2MB.")
        return file