# Generated by Django 4.0.3 on 2022-08-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_schoolmanagementcommittee_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherandstaff',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
