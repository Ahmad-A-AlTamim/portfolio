from django.db import models
from .models import account

class education(models.Model):
    degreeList = [
        ('High School','High School'),
        ('Diploma','Diploma'),
        ('Bachelor','Bachelor'),
        ('Master','Master'),
        ('Doctorate','Doctorate'),
        ('NanoDegree','NanoDegree'),
    ]
    degree = models.CharField(max_length=50,choices=degreeList,default='Bachelor')
    major = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    note = models.TextField()
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    def __str__(self):
        return self.major
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'