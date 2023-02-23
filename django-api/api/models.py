from django.db import models

class Attorney(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    cna = models.CharField(max_length=9)

    def __str__(self):
        return self.name