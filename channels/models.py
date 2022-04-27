from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    frequency = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
