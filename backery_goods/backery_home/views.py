from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    message = "Welcome to our bakery website!"
    return HttpResponse(message)
 