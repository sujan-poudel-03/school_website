# Generated by Django 4.0.3 on 2022-07-31 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='image',
            field=models.ImageField(upload_to='facilities'),
        ),
    ]
