from unicodedata import name
from django.contrib import admin
from django.urls import path
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='Home'),
    path('facilities', views.Facilities, name='Facilities'),
    path('result', views.Result, name='Result'),
    path('notice', views.Notice, name='Notice'),
    path('notice/<noticeId>', views.Notice, name='NoticeBoard'), # int , str , slug for dynamic routing
    path('aboutus', views.Aboutus, name='Aboutus'),
    path('contact', views.Contact, name='Contact'),
    path('principal message', views.PrincipalMessage, name='PrincipalMessage'),
    path('chairperson message', views.ChairpersonMesage, name='ChairpersonMessage')
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)