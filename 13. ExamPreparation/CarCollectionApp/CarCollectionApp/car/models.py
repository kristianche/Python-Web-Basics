from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import year_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2, 'The username must be a minimum of 2 chars')
        ],
        verbose_name='Username'
    )

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name='Email'
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Age',
        validators=[
            MinValueValidator(18)
        ]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        verbose_name='Password'
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )


class Car(models.Model):

    CAR_TYPES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )

    car_type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CAR_TYPES,
        verbose_name='Car Types'
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[MinLengthValidator(2)],
        verbose_name='Model'
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[year_validator],
        verbose_name='Year'
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)],
        verbose_name='Price'
    )


