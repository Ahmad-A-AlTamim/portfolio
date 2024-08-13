from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class account(models.Model):
    fname = models.CharField(max_length=50,verbose_name='First Name')
    lname = models.CharField(max_length=50,verbose_name='Last Name')
    phone = models.CharField(max_length=10,verbose_name='Phone Number')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/%H/%M/%S/',verbose_name='Profile Picture')
    birthdate = models.DateField(verbose_name='Birth Date')
    jopTitle = models.CharField(max_length=50,verbose_name='Jop Title')
    email = models.EmailField()
    Country = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    about = RichTextField(verbose_name='About me')
    logo = models.ImageField(upload_to='images/logo/%Y/%m/%d/%H/%M/%S/',verbose_name='Logo')
    cardBackground = models.ImageField(upload_to='images/logo/%Y/%m/%d/%H/%M/%S/',verbose_name='Card Background',default='static/assets/defaultBackGround/defaultBackGround.jpg')
    def __str__(self):
        return self.fname + ' ' + self.lname
