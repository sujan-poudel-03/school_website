# Generated by Django 4.0.3 on 2022-07-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_notice_file1_alter_notice_file2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file1',
            field=models.ImageField(blank=True, null=True, upload_to='news & notice'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file2',
            field=models.ImageField(blank=True, null=True, upload_to='news & notice'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file3',
            field=models.ImageField(blank=True, null=True, upload_to='news & notice'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='file4',
            field=models.ImageField(blank=True, null=True, upload_to='news & notice'),
        ),
    ]
