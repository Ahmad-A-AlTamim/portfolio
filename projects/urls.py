from django.urls import path
from . import views
urlpatterns = [
    path('', views.project, name='projects'),
    path('<str:title>', views.projectDetail, name='project'),
]