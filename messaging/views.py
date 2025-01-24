from django.shortcuts import render
from django.http import HttpResponse

def message_list(request):
    # Example response for a list of messages
    return HttpResponse("This is the message list.")

def message_detail(request, message_id):
    # Example response for message details
    return HttpResponse(f"This is the detail for message with ID {message_id}.")

