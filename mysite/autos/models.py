from django.core.validators import MinLengthValidator
from django.db import models


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a make (e.g. Dodge)',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname
