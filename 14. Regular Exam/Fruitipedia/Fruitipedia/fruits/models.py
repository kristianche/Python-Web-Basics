from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from .validators import only_letters, start_with_letter


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), MaxLengthValidator(25), start_with_letter],
        verbose_name='First Name'
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(1), MaxLengthValidator(35), start_with_letter],
        verbose_name='Last Name'
    )

    email = models.EmailField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(40)],
        verbose_name='Email'
    )

    password = models.CharField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(8), MaxLengthValidator(20)],
        verbose_name='Password'
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URl'
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
        verbose_name='Age',
        validators=[MinValueValidator(1)]
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), MaxLengthValidator(30), only_letters],
        verbose_name='First Name'
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Description'
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name='Nutrition'
    )


