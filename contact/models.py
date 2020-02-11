from django.db import models
from django.urls import reverse
class add(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    relation=models.CharField(max_length=20)
def __str__(self):
    return self.title
def	get_absolute_url(self): 
    return	reverse('detail')



