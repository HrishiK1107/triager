from django import forms
from .models import BugReport
import os

# Allowed file types for PoC uploads
ALLOWED_EXTENSIONS = ['.pdf', '.txt', '.zip', '.md']

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'cvss_score', 'poc_file']

    def clean_poc_file(self):
        file = self.cleaned_data.get('poc_file')
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                raise forms.ValidationError("Unsupported file type. Only PDF, TXT, ZIP, or MD allowed.")
        return file