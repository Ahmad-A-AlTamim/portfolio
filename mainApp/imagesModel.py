from django.db import models
from .models import account

class imagesModel(models.Model):
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d/%H/%M/%S')
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.image.url
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'