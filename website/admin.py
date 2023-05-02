from django.contrib import admin
from .models import notice, facilities, gallery, schoolmanagementcommittee, studentsview, teacherandstaff, studentsview
# Register your models here.
admin.site.register(notice),
admin.site.register(facilities),
admin.site.register(schoolmanagementcommittee),
admin.site.register(teacherandstaff),
admin.site.register(gallery),
admin.site.register(studentsview)
