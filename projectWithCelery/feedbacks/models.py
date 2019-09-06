from django.db import models

class EmailCreator(models.Model):
    email = models.EmailField(blank=False)
    name = models.CharField(max_length=300,blank=False)
    age = models.IntegerField(blank=True)
