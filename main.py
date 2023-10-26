import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from jobs.models import JobListing

# Initialize the MongoDB client and connect to a database
client = MongoClient("mongodb://localhost:27017/")
db = client["jobscraper_db"]
collection = db["job_listings"]

# Skills & Place of Work
skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the # of pages to scrape: '))

indeed_posts = []

for page in range(no_of_pages):
    # Connecting to India Indeed
    url = 'https://www.indeed.co.in/jobs?q=' + skill + '&l=' + place + '&sort=date' + '&start=' + str(page * 10)

    # Get request to indeed with headers above (you don't need headers!)
    response = requests.get(url)
    html = response.text

    # Scraping the Web (you can use 'html' or 'lxml')
    soup = BeautifulSoup(html, 'lxml')

    # Outer Most Entry Point of HTML:
    outer_most_point = soup.find('div', attrs={'id': 'mosaic-provider-jobcards'})

    # "UL" lists where the data is stored:
    for i in outer_most_point.find('ul'):
        # Job Title:
        job_title = i.find('h2', {'class': 'jobTitle jobTitle-color-purple jobTitle-newJob'})
        if job_title:
            jobs = job_title.find('a').text

        # Company Name:
        if i.find('span', {'class': 'companyName'}):
            company = i.find('span', {'class': 'companyName'}).text

        # Links: these Href links will take us to full job description
        if i.find('a'):
            links = i.find('a', {'class': 'jcs-JobTitle'})['href']

        # Salary if available:
        salary = i.find('div', {'class': 'salary-snippet'})

        if salary:
            salary_text = salary.text.strip()
        else:
            salary_text = 'No Salary'

        # Job Post Date:
        post_date = i.find('span', attrs={'class': 'date'}).text

        # Create and save a JobListing object
        job = JobListing(
            company=company,
            job_title=jobs,
            job_link=links,
            salary=salary_text,
            job_posted_date=post_date,
            text_description=""
        )
        job.save()

        # Put everything together in a list of lists for the default dictionary
        indeed_posts.append([company, jobs, links, salary_text, post_date])

# Close the MongoDB client connection
client.close()
