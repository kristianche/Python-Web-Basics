# Generated by Django 4.2.2 on 2023-06-24 06:56

import Fruitipedia.fruits.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(30), Fruitipedia.fruits.validators.only_letters], verbose_name='First Name')),
                ('image_url', models.URLField(verbose_name='Image URl')),
                ('description', models.TextField(verbose_name='Description')),
                ('nutrition', models.TextField(blank=True, null=True, verbose_name='Nutrition')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(25), Fruitipedia.fruits.validators.start_with_letter], verbose_name='First Name')),
                ('last_name', models.CharField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(35), Fruitipedia.fruits.validators.start_with_letter], verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.MaxLengthValidator(40)], verbose_name='Email')),
                ('password', models.CharField(validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(20)], verbose_name='Password')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URl')),
                ('age', models.IntegerField(blank=True, default=18, null=True, verbose_name='Age')),
            ],
        ),
    ]