from django.shortcuts import render
from users.models import PermissionModel,Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel
from django.contrib.auth.models import User
# Create your views here.
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from users.models import PermissionModel
from wsgiref.util import FileWrapper
import mimetypes



def download(request,id):
    print("----------------------------")
    print (PermissionModel.objects.get(id=id).resume)
    file_name=PermissionModel.objects.get(id=id).resume
    file_path = settings.MEDIA_ROOT +'/'+ str(file_name)
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(file_path)

    return response

def smart_str(x):
    if isinstance(x, str):
        return str(x).encode("utf-8")
    elif isinstance(x, int) or isinstance(x, float):
        return str(x)
    return x

def hrhome(request):

    return render(request, 'hrpanel/hrbase.html')

def freshersprofile(request):

    user=User.objects.all()
    per=PermissionModel.objects.select_related('user').all()

    print(user)
    for p in per:
        print(per)
        print(p.resume)
    # projects = Project.objects.select_related('user').all()
    # for project in projects:
    #     print project.name, project.leader.user_name
    #
    context={
    'user':user,
    'per':per
    }

    return render(request, 'hrpanel/freshersprofile.html',context)

def addtechnicalteam(request):

    return render(request, 'hrpanel/addtechnicalteam.html')

def candidatetracker(request):

    return render(request, 'hrpanel/candidatetracker.html')

def createnewjob(request):

    return render(request, 'hrpanel/createnewjob.html')


def experienceprofile(request):

    return render(request, 'hrpanel/experienceprofile.html')


def mail(request):

    return render(request, 'hrpanel/mail.html')

def offlineuser(request):

    return render(request, 'hrpanel/offlineuser.html')

def postjob(request):

    return render(request, 'hrpanel/postjob.html')

def shortlisted(request):

    return render(request, 'hrpanel/shortlisted.html')
