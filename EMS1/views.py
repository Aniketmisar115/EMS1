#I have created this file - Aniket
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Aniket ")

def home(request):
    return HttpResponse(" Welcome to our page ")
    
def about(request):
    return HttpResponse("About page ")