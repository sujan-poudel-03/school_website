from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from website.models import notice,facilities, schoolmanagementcommittee, teacherandstaff, gallery,studentsview
# Create your views here.
def Home(request):
    notice_object = notice.objects.order_by('-published_Date')
    gallery_object = gallery.objects.all()
    principal = schoolmanagementcommittee.objects.filter(post='Secretary')
    facilities_object = facilities.objects.all()
    studentview_latest = studentsview.objects.last()
    student_view = studentsview.objects.order_by("-id")[1:]
    return render(request, 'index.html', {'notice_object': notice_object, 'studentview_latest':studentview_latest, 'student_view': student_view, 'gallery_object':gallery_object, 'facilities_object': facilities_object, 'principal': principal })

def Result(request):
    return render(request, 'gallery.html')

def Facilities(request):
    facilities_obj = facilities.objects.all()
    # print(facilities_obj)
    return render(request, 'facilities.html', {'facilities_obj':facilities_obj})

def Notice(request, noticeId=''):
    print('Notice ID = ',noticeId)
    notice_board = notice.objects.order_by('-published_Date')[:1]
    allNotice_obj = notice.objects.order_by('-published_Date')
    noticeCount = notice.objects.all().count()
    # print(noticeCount)
    # ordered_notice = notice.objects.order_by('-published_Date')
    # Notice redirect from Index page using dynamic route
    if noticeId != '':
        redirectNotice = notice.objects.get(id=noticeId)
        print('hello',redirectNotice.noticeTitle)
    else:
        redirectNotice = None

    paginator = Paginator(allNotice_obj, 2)  # show 3 notices per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_page = page_obj.paginator.num_pages
    data = {
        'notice_board':notice_board,
        'noticeCout': noticeCount,
        'page_obj':page_obj, 
        'allNotice_obj': allNotice_obj,
        'redirectNotice':redirectNotice,
        'page_obj': page_obj,
        'last_page':total_page,
        'total_page_list': [n+1 for n in range(total_page)]
    }
    return render(request, 'notice.html', data)

def Aboutus(request):
    # smc_obj = schoolmanagementcommittee.objects.values_list('name', 'post')
    chairperson = schoolmanagementcommittee.objects.filter(post='Chairperson')
    secretary = schoolmanagementcommittee.objects.filter(post='Secretary')
    member = schoolmanagementcommittee.objects.filter(post='Member')
    ts_obj = teacherandstaff.objects.all()
    return render(request, 'aboutus.html', { 'chairperson':chairperson, 'secretary':secretary, 'member': member, 'ts_obj':ts_obj})

def Contact(request):
    return render(request, 'contact.html')

def PrincipalMessage(request):
    principal = schoolmanagementcommittee.objects.filter(post='Secretary')
    return render(request, 'principalMessage.html', {'principal':principal})

def ChairpersonMesage(request):
    chairperson = schoolmanagementcommittee.objects.filter(post='Chairperson')
    return render(request, 'chairpersonMessage.html', {'chairperson':chairperson})