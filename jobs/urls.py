from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('search/', views.search_jobs, name='search_jobs'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('average-salary/<str:user_city>/',views.average_salary_in_city, name='average_salary_in_city'),

]
