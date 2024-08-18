from django.db import models
from mainApp.models import account
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/projects/%Y/%m/%d/%H/%M/%S")
    url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title