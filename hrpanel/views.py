from django.shortcuts import render,redirect
from users.models import PermissionModel,Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel
from .models import ShortlistedCandiateModel
from django.contrib.auth.models import User
from .forms import ShortlistedCandidateDetailsForm
# Create your views here.
import os
import time

from django.conf import settings
from django.http import HttpResponse, Http404
from users.models import PermissionModel
from wsgiref.util import FileWrapper
import mimetypes
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

def addfreshershortlist(request,id):
    username=PermissionModel.objects.select_related('user').get(id=id)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(0.5)

    createddate=dt_string
    updateddate=dt_string


    t=ShortlistedCandiateModel(user=request.user,candiatename = username,createddate=createddate,updateddate=updateddate)
    t.save()
    request.user.shortlistedcandiatemodel.add(t)
    messages.success(request, f'Your account has been saved!{id}')
    return redirect('hrpanel-freshersprofile')



def download(request,id):

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
    # start Page nation
    users=User.objects.all()
    c = request.GET.get('page', 1)
    per=PermissionModel.objects.select_related('user').all()

    paginator = Paginator(per, 3)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    # end Page nation

    if request.method == 'POST':
        candiate_form = ShortlistedCandidateDetailsForm(request.POST)

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(0.5)
        createddate=dt_string
        updateddate=dt_string
        for p in per:

            try:
                flag = request.POST[str(p.id)]

                if flag=="on":
                    if request.POST["jobid"+str(p.id)] =="" or request.POST["jobid"+str(p.id)].isspace():
                        messages.error(request,f'Oops str({p.id}) we cant shortlist, Job id not selected kindly add it')
                        break
                    else:
                        jobid=request.POST["jobid"+str(p.id)]
                        if not ShortlistedCandiateModel.objects.filter(candiatename=p.user.username,jobid=jobid).exists():
                            t=ShortlistedCandiateModel(user=request.user,candiatename = str(p.user),jobid=jobid,createddate=createddate,updateddate=updateddate)
                            t.save()
                            request.user.shortlistedcandiatemodel.add(t)
                            messages.success(request, f'user is short listed !str({p.id})')
                            break
                        else:
                            messages.warning(request, f'user is alredy in short listed list !str({p.id})')
                            break
            except:
                pass

    else:
        candiate_form = ShortlistedCandidateDetailsForm()

    context={
    'users':users,
    'per':page,
    'candiate_form':candiate_form
    }

    return render(request, 'hrpanel/freshersprofile.html',context)

def experienceprofile(request):

    return render(request, 'hrpanel/experienceprofile.html')

def addtechnicalteam(request):

    return render(request, 'hrpanel/addtechnicalteam.html')

def candidatetracker(request):

    return render(request, 'hrpanel/candidatetracker.html')

def createnewjob(request):

    return render(request, 'hrpanel/createnewjob.html')




def mail(request):

    return render(request, 'hrpanel/mail.html')

def offlineuser(request):

    return render(request, 'hrpanel/offlineuser.html')

def postjob(request):

    return render(request, 'hrpanel/postjob.html')

def shortlisted(request):

    return render(request, 'hrpanel/shortlisted.html')
