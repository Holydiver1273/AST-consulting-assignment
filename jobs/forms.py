from django import forms
from .models import JobListing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['company', 'job_title', 'job_link', 'salary', 'job_posted_date', 'text_description']
