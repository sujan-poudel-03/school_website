# Generated by Django 4.0.3 on 2022-07-30 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_file4_notice_file4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='noticeTitle',
            new_name='notice_Title',
        ),
    ]
