from django.db import models
from django.db import models

class JobListing(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    job_link = models.URLField()
    salary = models.FloatField()  # Use FloatField to store salary as numbers
    job_posted_date = models.DateField()
    text_description = models.TextField()
    city = models.CharField(max_length=100)  # Add a field to store the city

    def __str__(self):
        return self.job_title


class JobListing(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    job_link = models.URLField()
    salary = models.FloatField()  # Store salaries as numbers
    job_posted_date = models.DateField()
    text_description = models.TextField()
    city = models.CharField(max_length=100)  # Add a field to store the city

    def __str__(self):
        return self.job_title
      
