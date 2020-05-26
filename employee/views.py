from django.shortcuts import render
from . forms import EmployeeEduDetailsForm
from . models import EmployeeEduDetailsModel
from django.contrib import messages
from django.shortcuts import render, redirect,reverse,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def employeeAddEdudetails(request):
    lst = []
    for n in range(1900,2020):
        lst.append(n)




    # print("------------------------------")
    # if request.method == 'POST':
    #     print('in post')
    #     e_form = EmployeeEduDetailsForm(request.POST,
    #                                request.user)
    #     print(e_form)
    #     if e_form.is_valid():
    #
    #         institutionname = e_form.cleaned_data["institutionname"]
    #         specialization = e_form.cleaned_data["specialization"]
    #         yearofpassing = e_form.cleaned_data["yearofpassing"]
    #         score = e_form.cleaned_data["score"]
    #         qualification = e_form.cleaned_data["qualification"]
    #         t=EmployeeEduDetailsModel(user=request.user,institutionname = institutionname,
    #         specialization =specialization,yearofpassing=yearofpassing,score=score,qualification=qualification)
    #         t.save()
    #         request.user.employeeedudetailsmodel.add(t)
    #         messages.success(request, f'Your account has been created! You are now able to log in')
    #
    #         return redirect('employeeAddEdudetails')
    #     else:
    #         print(e_form.errors)
    # else:
    #     e_form = EmployeeEduDetailsForm()
    # context={
    # 'e_form':e_form,
    #
    # }

    c = request.GET.get('page', 1)
    alldata=EmployeeEduDetailsModel.objects.filter(user=request.user).order_by('-id')

    paginator = Paginator(alldata, 10)

    try:
        page = paginator.page(c)

    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    if request.method == 'POST':

        e_form = EmployeeEduDetailsForm(request.POST)
        if e_form.is_valid():
            isSave=False
            try:
                technicalid=request.POST.get("eduid")
                print(technicalid)
                edit=technicalid.split('-')

                if edit[0] == 'edit':

                    offlinels=EmployeeEduDetailsModel.objects.get(id=edit[1])

                    offlinels.institutionname=request.POST.get("institutionname")
                    offlinels.specialization=request.POST.get("specialization")
                    offlinels.yearofpassing=request.POST.get("yearofpassing")
                    offlinels.score=request.POST.get("score")
                    offlinels.qualification=request.POST.get("qualification")
                    offlinels.save()

                    offlinels.save(update_fields=['institutionname'])
                    offlinels.save(update_fields=['specialization'])
                    offlinels.save(update_fields=['yearofpassing'])
                    offlinels.save(update_fields=['score'])

                    offlinels.save(update_fields=['qualification'])
                    messages.success(request, f'{request.POST.get("institutionname")} is updated success fully !')

                    return redirect('employeeAddEdudetails')

                elif edit[0] == 'delete':
                    print('lllll')
                    EmployeeEduDetailsModel.objects.get(id=edit[1]).delete()
                    messages.warning(request, f'{request.POST.get("institutionname")} is deleted success fully !')

                    return redirect('employeeAddEdudetails')

            except:
                isSave=True

                # Update data in Db
            if isSave:
                print('save')
                institutionname=e_form.cleaned_data["institutionname"]
                specialization = e_form.cleaned_data["specialization"]
                yearofpassing = e_form.cleaned_data["yearofpassing"]
                score = e_form.cleaned_data["score"]
                qualification = e_form.cleaned_data["qualification"]
                t=EmployeeEduDetailsModel(user=request.user,
                institutionname=institutionname,specialization=specialization,yearofpassing=yearofpassing,
                score=score,qualification=qualification)
                t.save()
                messages.success(request, f'{institutionname} is added success fully !')
                return redirect('employeeAddEdudetails')

        else:
            print(e_form.errors)
    else:
        e_form = EmployeeEduDetailsForm()


    context={
    'e_form':e_form,
    'technicalset':page,
    'lst':lst,
    }


    return render(request, 'employee/employeeAddEdudeatils.html',context)
