from django.shortcuts import render,redirect
from users.models import PermissionModel,Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel
from .models import ShortlistedCandiateModel,CreateNewJobModel
from django.contrib.auth.models import User
from .forms import ShortlistedCandidateDetailsForm,CreateNewJobForm
# Create your views here.
import os
import time
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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

    print('pls use form in tr tag')
    print('https://stackoverflow.com/questions/34998769/django-dynamic-name-attribute-and-getting-values-in-views-py')

    return render(request, 'hrpanel/experienceprofile.html')

def addtechnicalteam(request):

    return render(request, 'hrpanel/addtechnicalteam.html')

def candidatetracker(request):

    return render(request, 'hrpanel/candidatetracker.html')

def createnewjob(request):

    jobset=CreateNewJobModel.objects.filter(user=request.user)

    if request.method == 'POST':

        job_form = CreateNewJobForm(request.POST)
        if job_form.is_valid():
            jobid = job_form.cleaned_data["jobid"]
            jobtitle = job_form.cleaned_data["jobtitle"]
            experience = job_form.cleaned_data["experience"]
            clientname=job_form.cleaned_data["clientname"]
            companyname = job_form.cleaned_data["companyname"]
            mandatoryskils = job_form.cleaned_data["mandatoryskils"]
            designation = job_form.cleaned_data["designation"]
            expectednoticeperiod =job_form.cleaned_data["expectednoticeperiod"]
            jobdescription = job_form.cleaned_data["jobdescription"]
            domain = job_form.cleaned_data["domain"]
            joblocation = job_form.cleaned_data["joblocation"]
            contactname=job_form.cleaned_data["contactname"]
            contactmailid = job_form.cleaned_data["contactmailid"]
            contactmobilenumber = job_form.cleaned_data["contactmobilenumber"]
            payscalefromlacks = job_form.cleaned_data["payscalefromlacks"]
            payscalefromthousand=job_form.cleaned_data["payscalefromthousand"]
            payscaletolacks = job_form.cleaned_data["payscaletolacks"]
            payscaletothousand = job_form.cleaned_data["payscaletothousand"]
            contractjob = job_form.cleaned_data["contractjob"]
            contractfromyear=job_form.cleaned_data["contractfromyear"]
            contractfrommonth = job_form.cleaned_data["contractfrommonth"]
            contracttoyear = job_form.cleaned_data["contracttoyear"]
            contracttomonth = job_form.cleaned_data["contracttomonth"]

            t=CreateNewJobModel(user=request.user,
            jobid=jobid,jobtitle=jobtitle,experience=experience,
            clientname=clientname,companyname=companyname,mandatoryskils=mandatoryskils,designation=designation,
            expectednoticeperiod=expectednoticeperiod,jobdescription=jobdescription,domain=domain,joblocation=joblocation,
            contactname=contactname,contactmailid=contactmailid,contactmobilenumber=contactmobilenumber,
            payscalefromlacks=payscalefromlacks,payscalefromthousand=payscalefromthousand,
            payscaletolacks=payscaletolacks,payscaletothousand=payscaletothousand,contractjob=contractjob,
            contractfromyear=contractfromyear,contractfrommonth=contractfrommonth,contracttoyear=contracttoyear,contracttomonth=contracttomonth
            )
            t.save()
            messages.success(request, f'Your new job id is generated!')
            print(">>>>>>>>>>>>>>> Saved")
            return redirect('hrpanel-viewcreatenewjob',jobid=jobid)
        else:
            print(job_form.errors)

    else:
        job_form = CreateNewJobForm()
    context={
    'job_form':job_form,
    'jobset':jobset
    }
    return render(request, 'hrpanel/createnewjob.html',context=context)

@login_required
def viewcreatenewjob(request,jobid):

    lastjobid=CreateNewJobModel.objects.filter(jobid=jobid)[0]
    print(lastjobid)
    context={
    'lastjobid':lastjobid
    }
    return render(request, 'hrpanel/viewcreatenewjob.html',context=context)

@login_required
def updatecreatenewjob(request, jobid):

    jobset=CreateNewJobModel.objects.filter(jobid=jobid)
    jobls=CreateNewJobModel.objects.get(jobid=jobid)

    print(jobset)
    print(jobls)

    if  request.method=='POST':
        print("form Post")
        job_form = CreateNewJobForm(request.POST)
        if job_form.is_valid():
            print("form valid")
            if jobset:
                jobls=CreateNewJobModel.objects.get(jobid=jobid)
                updateid=request.POST.get("jobid")
                print(updateid)
                print(jobid)
                jobls.jobid=request.POST.get("jobid")
                jobls.jobtitle=request.POST.get("jobtitle")
                jobls.experience=request.POST.get("experience")
                jobls.clientname=request.POST.get("clientname")
                jobls.companyname=request.POST.get("companyname")
                jobls.mandatoryskils=request.POST.get("mandatoryskils")
                jobls.designation=request.POST.get("designation")
                jobls.expectednoticeperiod=request.POST.get("expectednoticeperiod")
                jobls.jobdescription=request.POST.get("jobdescription")
                jobls.domain=request.POST.get("domain")
                jobls.joblocation=request.POST.get("joblocation")
                jobls.contactname=request.POST.get("contactname")
                jobls.contactmailid=request.POST.get(" contactmailid")
                jobls.contactmobilenumber=request.POST.get("contactmobilenumber")
                jobls.payscalefromlacks=request.POST.get("payscalefromlacks")
                jobls.payscalefromthousand=request.POST.get("payscalefromthousand")
                jobls.payscaletolacks=request.POST.get("payscaletolacks")
                jobls.payscaletothousand=request.POST.get("payscaletothousand")
                jobls.contractjob=request.POST.get("contractjob")
                jobls.contractfromyear=request.POST.get("contractfromyear")
                jobls.contractfrommonth=request.POST.get("contractfrommonth")
                jobls.contracttoyear=request.POST.get("contracttoyear")
                jobls.contracttomonth=request.POST.get("contracttomonth")

                jobls.save()
                # Update data in Db
                jobls.save(update_fields=['jobid'])
                jobls.save(update_fields=['jobtitle'])
                jobls.save(update_fields=['experience'])
                jobls.save(update_fields=['clientname'])
                jobls.save(update_fields=['companyname'])
                jobls.save(update_fields=['mandatoryskils'])
                jobls.save(update_fields=['designation'])
                jobls.save(update_fields=['expectednoticeperiod'])
                jobls.save(update_fields=['jobdescription'])
                jobls.save(update_fields=['domain'])
                jobls.save(update_fields=['joblocation'])
                jobls.save(update_fields=['contactname'])
                jobls.save(update_fields=['contactmailid'])
                jobls.save(update_fields=['contactmobilenumber'])
                jobls.save(update_fields=['payscalefromlacks'])
                jobls.save(update_fields=['payscalefromthousand'])
                jobls.save(update_fields=['payscaletolacks'])
                jobls.save(update_fields=['payscaletothousand'])
                jobls.save(update_fields=['contractjob'])
                jobls.save(update_fields=['contractfromyear'])
                jobls.save(update_fields=['contractfrommonth'])
                jobls.save(update_fields=['contracttoyear'])
                jobls.save(update_fields=['contracttomonth'])
                messages.success(request, f'Your current job id {updateid} is updated successfully')


                return redirect('hrpanel-viewcreatenewjob',jobid=updateid)
        else:
            messages.error(request, f'Kindly fill all required fileds')
    else:
        job_form = CreateNewJobForm()
    context = {
        'job_form': job_form,
        'jobset':jobset,
        'jobls':jobls
        }
    return render(request, 'hrpanel/updatecreatenewjob.html',context=context)



def mail(request):

    return render(request, 'hrpanel/mail.html')

def offlineuser(request):

    return render(request, 'hrpanel/offlineuser.html')

def postjob(request):
    c = request.GET.get('page', 1)
    allcreatedjob=CreateNewJobModel.objects.filter(user=request.user).order_by('-id')

    paginator = Paginator(allcreatedjob, 3)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context={
    'allcreatedjob':allcreatedjob,
    'per':page,

    }

    return render(request, 'hrpanel/postjob.html',context)




def shortlisted(request):



    c = request.GET.get('page', 1)
    allshortlisted=ShortlistedCandiateModel.objects.all()

    paginator = Paginator(allshortlisted, 3)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context={
    'allshortlisted':allshortlisted,
    'per':page,

    }
    return render(request, 'hrpanel/shortlisted.html',context)
