from django.db import models

# Create your models here.
class Sample(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.title
