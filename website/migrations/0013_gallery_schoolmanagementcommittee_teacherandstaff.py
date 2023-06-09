# Generated by Django 4.0.3 on 2022-08-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_notice_file1_alter_notice_file2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desciption', models.TextField()),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='schoolmanagementcommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=20)),
                ('post', models.CharField(choices=[('Cp', 'Chairperson'), ('Sec', 'Secretary'), ('Mem', 'Member')], max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='teacherandstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=20)),
                ('role', models.CharField(choices=[('Cp', 'Chairperson'), ('Sec', 'Secretary'), ('Mem', 'Member')], max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('education', models.TextField()),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
