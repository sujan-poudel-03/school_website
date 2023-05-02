# Generated by Django 4.0.3 on 2022-07-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_Title', models.CharField(max_length=255)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Published_Date', models.DateTimeField(auto_now_add=True)),
                ('Update_Date', models.DateTimeField(auto_now=True)),
                ('File', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
