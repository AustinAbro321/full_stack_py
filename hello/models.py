from django.db import models

# Create your models here.
class greeting(models.Model):
    greeting = models.CharField(max_length=200)

    def __str__(self):
        return self.greeting