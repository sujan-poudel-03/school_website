# Generated by Django 4.0.3 on 2022-07-30 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_notice_title_notice_noticetitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='file5',
        ),
    ]
