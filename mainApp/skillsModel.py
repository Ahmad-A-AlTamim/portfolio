from django.db import models
from .models import account
class skills(models.Model):
    categoryList = [
        ('Software Programming Skills','Software Programming Skills'),
        (' Operating Systems',' Operating Systems'),
        ('Editors','Editors'),
        ('IDEs','IDEs'),
        ('Design','Design'),
    ]
    category = models.CharField(max_length=50,choices=categoryList,default='Software Programming Skills')
    skill = models.CharField(max_length=50)
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    def __str__(self):
        return self.skill
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'