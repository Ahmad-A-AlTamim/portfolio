from django.shortcuts import render
from .models import account
def index(request):

    return render(request, 'pages/mainPage.html')
def project(request):

    return render(request, 'pages/projects.html')
# Create your views here.
