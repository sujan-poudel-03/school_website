# Generated by Django 4.0.3 on 2022-08-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_schoolmanagementcommittee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='facilities'),
        ),
    ]
