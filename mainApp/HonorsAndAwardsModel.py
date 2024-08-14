from django.db import models
from .models import account
class honorsAndAwards(models.Model):
    title = models.CharField(max_length=50)
    rank=models.CharField(max_length=50)
    date=models.DateField()
    description = models.TextField()
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Honor and Award'
        verbose_name_plural = 'Honors and Awards'