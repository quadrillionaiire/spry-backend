from django.shortcuts import render
from django.http import HttpResponse

def job_list(request):
    # Example response for a list of jobs
    return HttpResponse("This is the job list.")

def job_detail(request, job_id):
    # Example response for job details
    return HttpResponse(f"This is the detail for job with ID {job_id}.")

