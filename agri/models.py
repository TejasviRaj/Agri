from django.db import models

# Create your models here.

from django.db import models

class soilfield(models.Model):
    area=models.FloatField()
    irrigation=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
