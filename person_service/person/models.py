from django.db import models


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
        return f'{self.number} {self.street} {self.city} {self.state}'


class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.ForeignKey(
        Address, related_name="person", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name} {self.email} {self.address}'
