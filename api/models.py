from django.db import models

# Create your models here.
class Model(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

    def __str__(self):
        return self.FirstName
