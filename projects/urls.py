from django.urls import path
from . import views
urlpatterns = [
    path('', views.project, name='projects'),
    path('<int:id>', views.projectDetail, name='project'),
]