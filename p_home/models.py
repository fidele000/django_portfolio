from django.db import models

# Create your models here.

class Info(models.Model):

    name=models.CharField(max_length=50)
    carrer_title=models.CharField(max_length=100)
    about_me=models.TextField(default='')
    location=models.CharField(max_length=60)
    email=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=13)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'