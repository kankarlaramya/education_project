from django.db import models

class task(models.Model):
    def __str__(self):
        return self.title

# Create your models here.
    title = models.CharField(max_length = 40)
    desc_1= models.CharField(max_length = 200)
    desc_2= models.CharField(max_length = 200)
    desc_3= models.CharField(max_length = 200)


