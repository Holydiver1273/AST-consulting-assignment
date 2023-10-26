from jobs.models import JobListing
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .forms import JobListingForm
from pymongo import MongoClient

# Initialize the MongoDB client and connect to a database
client = MongoClient("mongodb://localhost:27017/")  # Modify the URL to your MongoDB instance
db = client["jobscraper_db"]  # Use your preferred database name

def scrape_and_save_jobs(request):
    # Initialize the MongoDB client and connect to a database
    client = MongoClient("mongodb://localhost:27017/")  # Modify the URL to your MongoDB instance
    db = client["jobscraper_db"]

    # Create a collection to store job listings
    collection = db["job_listings"]

    # Your web scraping code here (integrate the MongoDB code for saving job listings)

    # Calculate average salary for Python developers in the user's city
    user_city = request.GET.get('city', '')
    average_salary = JobListing.objects.filter(
        job_title__icontains='python developer',
        city=user_city
    ).aggregate(Avg('salary'))['salary__avg']

    # Close the MongoDB client connection
    client.close()

    # Other view logic or return a response as needed


# Create a collection to store job listings
collection = db["job_listings"]
def search_jobs(request):
    user_city = request.GET.get('city', '')  # Get the user's city from the request
    python_dev_jobs = JobListing.objects.filter(
        job_title__icontains='python developer',
        location=user_city  
    )

    return render(request, 'jobs/job_search.html', {'python_dev_jobs': python_dev_jobs})


def edit_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    
    if request.method == 'POST':
        form = JobListingForm(request.POST, instance=job)  # Bind the form to the existing job instance
        if form.is_valid():
            form.save()  # Save the changes to the job listing
            return redirect('search_jobs')  # Redirect to the search results or another appropriate page
    else:
        form = JobListingForm(instance=job)  # Create an instance of the form with the existing data

    return render(request, 'jobs/edit_job.html', {'job': job, 'form': form})

def delete_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    if request.method == 'POST':
        # Handle job deletion
        job.delete()
        return redirect('search_jobs')  # Redirect to the search page or another page
    return render(request, 'jobs/delete_job.html', {'job': job})

def average_salary_in_city(request, user_city):
    average_salary = JobListing.objects.filter(
        job_title__icontains='python developer',
        city=user_city  # Use the field you added to specify the user's city
    ).aggregate(Avg('salary'))['salary__avg']

    return render(request, 'jobs/average_salary.html', {'average_salary': average_salary})

# Close the MongoDB client connection
client.close()


