# Generated by Django 4.2.1 on 2023-05-31 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_Players_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]