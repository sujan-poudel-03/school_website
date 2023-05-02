from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class notice(models.Model):
    noticeTitle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published_Date = models.DateTimeField('date created', default=timezone.now)
    update_Date = models.DateTimeField('date created', default=timezone.now)
    file1 = models.ImageField(blank=True, null=True, upload_to='news & notice')
    file2 = models.ImageField(blank=True, null=True, upload_to='news & notice')
    file3 = models.ImageField(blank=True, null=True, upload_to='news & notice')
    file4 = models.ImageField(blank=True, null=True, upload_to='news & notice')

    def __str__(self):
        return self.noticeTitle + ' -  ' + self.description + '   ->' + str(self.published_Date)

class gallery(models.Model):
    name = models.CharField(max_length=255)
    desciption = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False, upload_to='gallery')

    def __str__(self):
        return self.name + '  ' + self.desciption


class facilities(models.Model):
    name = models.CharField(max_length=255)
    desciption = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False, upload_to='facilities')

    def __str__(self):
        return self.name + '  ' + self.desciption

class studentsview(models.Model):
    name = models.CharField(max_length=255)
    additionalDetail = models.CharField(max_length=55)
    studentView = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True, upload_to='facilities')

    def __str__(self):
        return self.name + ' - ' + self.additionalDetail

Post = (
        ('Chairperson', 'Chairperson'),
        ('Secretary', 'Secretary'),
        ('Member', 'Member'),
    )
Gender = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
)
class schoolmanagementcommittee(models.Model):
    name = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=20, choices=Gender)
    post = models.CharField(max_length=15, choices=Post)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.post


class teacherandstaff(models.Model):
    name = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=20, choices=Gender)
    role = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    education = models.TextField(blank=False, null=False)
    subject = models.TextField(blank=False, null=False)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.role