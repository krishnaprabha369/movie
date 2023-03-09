from django.db import models



# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=25,blank=True)
    description = models.TextField(max_length=250,blank=True)
    year = models.IntegerField(default='0')
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name




