# Generated by Django 4.0.3 on 2022-07-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='File',
            new_name='File1',
        ),
        migrations.AddField(
            model_name='notice',
            name='File2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='notice',
            name='File3',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='notice',
            name='File4',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='notice',
            name='File5',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
