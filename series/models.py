from datetime import datetime, timedelta
from django.db import models

from channels.models import Channel

class Serie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ChannelSerie(models.Model):
    channel: Channel = models.ForeignKey(to=Channel, on_delete=models.RESTRICT)
    serie = models.ForeignKey(to=Serie, on_delete=models.CASCADE)
    time = models.TimeField()

    @property
    def channel_order(self):
        return self.channel.order
