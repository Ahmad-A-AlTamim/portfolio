from django.shortcuts import render
from .models import Project
def project(request):
    return render(request, 'pages/projects.html')

def projectDetail(request, id):
    project=Project.objects.get(id=id)
    context = {
        'project':project,
        'tech':project.technology.split(',')
    }
    return render(request, 'pages/projectPage.html',context)
# Create your views here.
