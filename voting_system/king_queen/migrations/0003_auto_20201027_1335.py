# Generated by Django 2.2 on 2020-10-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king_queen', '0002_auto_20201027_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstyear',
            name='img',
            field=models.ImageField(upload_to='kingqueenIMG'),
        ),
    ]
