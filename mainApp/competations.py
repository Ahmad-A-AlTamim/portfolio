from django.db import models
from  .models import account

class competations(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    account = models.ForeignKey(account, on_delete=models.CASCADE)
    def __str__(self):
        return self.name