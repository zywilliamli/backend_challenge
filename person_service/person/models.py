from django.db import models


# Create your models here.
class Address(models.Model):
    class AustralianStates(models.TextChoices):
        ACT = 'Australian Capital Territory'
        NSW = 'New South Wales'
        NT = 'Northern Territory'
        QLD = 'Queensland'
        SA = 'South Australia'
        VIC = 'Victoria'
        TAS = 'Tasmania'
        WA = 'Western Australia'

    number = models.PositiveIntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=AustralianStates.choices)

    def __str__(self):
        # todo: should we hash this?
        return self.name


class Person(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(
        Address, related_name="person", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
