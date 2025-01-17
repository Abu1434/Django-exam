from django.db import models


class OneModel(models.Model):
    name = models.CharField(max_length=50)


class TwoModel(models.Model):
    integer = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.integer} {self.date}'


class SpecialModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class PersonModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
