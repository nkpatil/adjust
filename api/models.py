from django.db import models


class Data(models.Model):
    """Stores data represents performance metrics
    (impressions, clicks, installs, spend, revenue)
    for a given date, advertising channel, country
    and operating system"""
    date = models.DateField()
    channel = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    class Meta:
        unique_together = ('date', 'channel', 'country', 'os')

    def __str__(self):
        return "{} : {} | {}".format(self.date, self.channel, self.os)
