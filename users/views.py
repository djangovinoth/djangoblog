from django.shortcuts import render, redirect,reverse,render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,EduDetailsUpdateForm,CompanyDetailsUpdateForm,PersonalDetailsUpdateForm,SkillSetDetailsUpdateForm,PermissionForm
# ,ProfileResumeUpdateForm,ProfileImageUpdateForm,ProfilePhoneUpdateForm
from .models import Profile,EdudetailsModel,CompanyDetailsModel,PersonalDetailsModel,SkillSetDetailsModel
from django.template import RequestContext


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PermissionForm(request.POST,
                                   request.FILES,
                                   instance=request.user.permissionmodel)

        if u_form.is_valid() and p_form.is_valid():
            print(p_form)
            user=u_form.save()
            p_form.save()

            messages.success(request, f'Your profile details have been updated!')
            return redirect('edudetails')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PermissionForm(instance=request.user.permissionmodel)


    context = {
        'u_form': u_form,
        'p_form': p_form
        }

    return render(request, 'users/profile.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your profile details have been updated!')
#             return redirect('edudetails')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#         }
#
#     return render(request, 'users/profile.html', context)
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form=PermissionForm(request.POST,request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user=u_form.save()
            per=p_form.save(commit=False)
            per.user=user
            per.save()

            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = PermissionForm()
    return render(request, 'users/register.html', {'u_form': u_form,'p_form':p_form})



@login_required
def deletecompany(request, id):
    companyset=CompanyDetailsModel.objects.filter(id=id)
    print(companyset)
    if companyset:

        companyset.delete()
        return redirect('addcompanyView')


    return render(request, 'users/addcompanyView.html',{'companyset':companyset})

@login_required
def updatecompany(request, id):

    companyset=CompanyDetailsModel.objects.filter(id=id)
    ls=CompanyDetailsModel.objects.get(id=id)

    if  request.method=='POST':
        print("form Post")
        company_form = CompanyDetailsUpdateForm(request.POST)
        if company_form.is_valid():
            print("form valid")
            if companyset:
                ls=CompanyDetailsModel.objects.get(id=id)
                print(ls)
                ls.companyname=request.POST.get("companyname")
                print(request.POST.get("companyname"))
                ls.exp=request.POST.get("exp")
                ls.save()
                # Update data in Db
                ls.save(update_fields=['companyname'])
                ls.save(update_fields=['exp'])
                return redirect('addcompanyView')
        else:
            print("not valid")
    else:
        company_form = CompanyDetailsUpdateForm()
    context = {
        'company_form': company_form,
        'companyset':companyset,
        'ls':ls
        }
    return render(request, 'users/updatecompany.html',context=context)

@login_required
def addcompanyView(request):
    companyset=CompanyDetailsModel.objects.filter(user=request.user).order_by('-id')
    print(companyset)
    if request.method == 'POST':
        company_form = CompanyDetailsUpdateForm(request.POST)
        if company_form.is_valid():
            companyname = company_form.cleaned_data["companyname"]
            exp = company_form.cleaned_data["exp"]
            t=CompanyDetailsModel(user=request.user,companyname = companyname,
            exp =exp)
            t.save()
            request.user.companydetailsmodel.add(t)
            messages.success(request, f'Your account has been saved!')
            return redirect('addcompanyView')
    else:
        company_form = CompanyDetailsUpdateForm()
    context = {
        'company_form': company_form,
        'companyset':companyset
        }
    return render(request, 'users/addcompany.html',context=context)



@login_required
def personaldetailsView(request):
    perdet=PersonalDetailsModel.objects.filter(user=request.user)[0]
    print(perdet)
    return render(request, 'users/personaldetailsView.html',{'perdet':perdet})

@login_required
def addpersonaldetails(request):
    isadded=False

    personalset=PersonalDetailsModel.objects.filter(user=request.user)
    if PersonalDetailsModel.objects.filter(user=request.user).count() ==0:
        isadded=True
    else:
        isadded=False

    if request.method == 'POST':

        personal_form = PersonalDetailsUpdateForm(request.POST)
        if personal_form.is_valid():
            firstName = personal_form.cleaned_data["firstName"]
            lastName = personal_form.cleaned_data["lastName"]
            fatherName = personal_form.cleaned_data["fatherName"]
            phoneNumber=personal_form.cleaned_data["phoneNumber"]

            gender = personal_form.cleaned_data["gender"]
            countryName = personal_form.cleaned_data["countryName"]
            dateOfBrith = personal_form.cleaned_data["dateOfBrith"]

            currentLocation =personal_form.cleaned_data["currentLocation"]

            panNumber = personal_form.cleaned_data["panNumber"]
            aatharNumber = personal_form.cleaned_data["aatharNumber"]
            currnetMailAddress = personal_form.cleaned_data["currnetMailAddress"]
            permanentMailAddress=personal_form.cleaned_data["permanentMailAddress"]


            t=PersonalDetailsModel(user=request.user,firstName = firstName,
            lastName =lastName,fatherName =fatherName,
            phoneNumber=phoneNumber,gender = gender, countryName = countryName,
            dateOfBrith =dateOfBrith,currentLocation =currentLocation,panNumber = panNumber,
            aatharNumber = aatharNumber, currnetMailAddress = currnetMailAddress,
            permanentMailAddress = permanentMailAddress)
            t.save()
            messages.success(request, f'Your account has been saved!')
            return redirect('personaldetailsView')
        else:
            print(personal_form.errors)

    else:
        personal_form = PersonalDetailsUpdateForm()
    context={
    'personal_form':personal_form,
    'personalset':personalset
    }
    if isadded:
        return render(request, 'users/addpersonaldetails.html',context=context)
    else:
        return redirect('personaldetailsView')

@login_required
def updatepersonaldetails(request):
    personalset=PersonalDetailsModel.objects.get(user=request.user)
    if request.method == 'POST':
        print("post is valid>>>>>>>>>>>>>>")
        personal_form = PersonalDetailsUpdateForm(request.POST)
        if personal_form.is_valid():
            personalset.firstName=request.POST.get("firstName")
            personalset.lastName=request.POST.get("lastName")
            personalset.fatherName=request.POST.get("fatherName")
            personalset.phoneNumber=request.POST.get("phoneNumber")
            personalset.gender=request.POST.get("gender")
            personalset.countryName=request.POST.get("countryName")
            personalset.dateOfBrith=request.POST.get("dateOfBrith")
            personalset.currentLocation=request.POST.get("currentLocation")
            personalset.panNumber=request.POST.get("panNumber")
            personalset.aatharNumber=request.POST.get("aatharNumber")
            personalset.currnetMailAddress=request.POST.get("currnetMailAddress")
            personalset.permanentMailAddress=request.POST.get("permanentMailAddress")
            personalset.save()
            # Update data in Db

            personalset.save(update_fields=['firstName'])
            personalset.save(update_fields=['lastName'])
            personalset.save(update_fields=['fatherName'])
            personalset.save(update_fields=['phoneNumber'])
            personalset.save(update_fields=['gender'])
            personalset.save(update_fields=['countryName'])
            personalset.save(update_fields=['dateOfBrith'])

            personalset.save(update_fields=['currentLocation'])
            personalset.save(update_fields=['panNumber'])
            personalset.save(update_fields=['aatharNumber'])
            personalset.save(update_fields=['currnetMailAddress'])
            personalset.save(update_fields=['permanentMailAddress'])


            messages.success(request, f'Your personal account has been Updated!')
            return redirect('personaldetailsView')
    else:
        personal_form = PersonalDetailsUpdateForm()
    context={
    'personal_form':personal_form,
    'personalset':personalset
    }
    return render(request, 'users/updatepersonaldetails.html',context=context)





@login_required
def edudetails(request):
    isadded=False

    if PersonalDetailsModel.objects.filter(user=request.user).count() ==0:
        isadded=True
    else:
        isadded=False


    if request.method == 'POST':
        u_form = EduDetailsUpdateForm(request.POST)
        if u_form.is_valid():
            schoolX = u_form.cleaned_data["schoolX"]
            specializationX = u_form.cleaned_data["specializationX"]
            yearOfPassingX = u_form.cleaned_data["yearOfPassingX"]
            scoreX=u_form.cleaned_data["scoreX"]

            schoolXII = u_form.cleaned_data["schoolXII"]
            specializationXII = u_form.cleaned_data["specializationXII"]
            yearOfPassingXII = u_form.cleaned_data["yearOfPassingXII"]
            scoreXII =u_form.cleaned_data["scoreXII"]

            diploma = u_form.cleaned_data["diploma"]
            specializationDiploma = u_form.cleaned_data["specializationDiploma"]
            yearOfPassingDiploma = u_form.cleaned_data["yearOfPassingDiploma"]
            scoreDiploma=u_form.cleaned_data["scoreDiploma"]

            UG = u_form.cleaned_data["UG"]
            specializationUG = u_form.cleaned_data["specializationUG"]
            yearOfPassingUG = u_form.cleaned_data["yearOfPassingUG"]
            scoreUG=u_form.cleaned_data["scoreUG"]

            PG = u_form.cleaned_data["PG"]
            specializationPG = u_form.cleaned_data["specializationPG"]
            yearOfPassingPG = u_form.cleaned_data["yearOfPassingPG"]
            scorePG=u_form.cleaned_data["scorePG"]
            EdudetailsModel.objects.get_or_create(user=request.user)

            if not EdudetailsModel.objects.get(user=request.user):
                print(' inserted')
                t=EdudetailsModel(user=request.user,schoolX = schoolX,
                specializationX =specializationX,yearOfPassingX =yearOfPassingX,
                scoreX=scoreX,schoolXII = schoolXII, specializationXII = specializationXII,
                yearOfPassingXII =yearOfPassingXII,scoreXII =scoreXII,diploma = diploma,
                specializationDiploma = specializationDiploma, yearOfPassingDiploma = yearOfPassingDiploma,
                scoreDiploma=scoreDiploma,UG = UG,specializationUG = specializationUG,
                yearOfPassingUG = yearOfPassingUG,scoreUG=scoreUG,PG = PG,
                specializationPG = specializationPG, yearOfPassingPG = yearOfPassingPG,scorePG=scorePG)
                t.save()
                request.user.edudetailsmodel.add(t)
                messages.success(request, f'Your account has been saved!')

            else:
                # Get data from form
                ls=EdudetailsModel.objects.get(user=request.user)

                ls.schoolX=request.POST.get("schoolX")
                ls.specializationX=request.POST.get("specializationX")
                ls.yearOfPassingX=request.POST.get("yearOfPassingX")
                ls.scoreX=request.POST.get("scoreX")

                ls.schoolXII=request.POST.get("schoolXII")
                ls.specializationXII=request.POST.get("specializationXII")
                ls.yearOfPassingXII=request.POST.get("yearOfPassingXII")
                ls.scoreXII=request.POST.get("scoreXII")

                ls.diploma=request.POST.get("diploma")
                ls.specializationDiploma=request.POST.get("specializationDiploma")
                ls.yearOfPassingDiploma=request.POST.get("yearOfPassingDiploma")
                ls.scoreDiploma=request.POST.get("scoreDiploma")


                ls.UG=request.POST.get("UG")
                ls.specializationUG=request.POST.get("specializationUG")
                ls.yearOfPassingUG=request.POST.get("yearOfPassingUG")
                ls.scoreUG=request.POST.get("scoreUG")

                ls.PG=request.POST.get("PG")
                ls.specializationPG=request.POST.get("specializationPG")
                ls.yearOfPassingPG=request.POST.get("yearOfPassingPG")
                ls.scorePG=request.POST.get("scorePG")
                ls.save()
                # Update data in Db

                ls.save(update_fields=['schoolX'])
                ls.save(update_fields=['specializationX'])
                ls.save(update_fields=['yearOfPassingX'])
                ls.save(update_fields=['scoreX'])

                ls.save(update_fields=['schoolXII'])
                ls.save(update_fields=['specializationXII'])
                ls.save(update_fields=['yearOfPassingXII'])
                ls.save(update_fields=['scoreXII'])

                ls.save(update_fields=['diploma'])
                ls.save(update_fields=['specializationDiploma'])
                ls.save(update_fields=['yearOfPassingDiploma'])
                ls.save(update_fields=['scoreDiploma'])

                ls.save(update_fields=['UG'])
                ls.save(update_fields=['specializationUG'])
                ls.save(update_fields=['yearOfPassingUG'])
                ls.save(update_fields=['scoreUG'])

                ls.save(update_fields=['PG'])
                ls.save(update_fields=['specializationPG'])
                ls.save(update_fields=['yearOfPassingPG'])
                ls.save(update_fields=['scorePG'])
                messages.success(request, f'Your account has been updated!')
            return redirect('edudetailsView')
        else:
            print (u_form.errors)

    else:
            u_form = EduDetailsUpdateForm()
    context = {
        'u_form': u_form,

        }
    if isadded:
        return render(request, 'users/edudetails.html', context)
    else:
        return redirect('edudetailsView')

@login_required
def updateedudetails(request):
    lst = []
    for n in range(1900,2020):
        lst.append(n)


    ls=EdudetailsModel.objects.get(user=request.user)

    if request.method == 'POST':
        u_form = EduDetailsUpdateForm(request.POST)
        if u_form.is_valid():
            schoolX = u_form.cleaned_data["schoolX"]
            specializationX = u_form.cleaned_data["specializationX"]
            yearOfPassingX = u_form.cleaned_data["yearOfPassingX"]
            scoreX=u_form.cleaned_data["scoreX"]

            schoolXII = u_form.cleaned_data["schoolXII"]
            specializationXII = u_form.cleaned_data["specializationXII"]
            yearOfPassingXII = u_form.cleaned_data["yearOfPassingXII"]
            scoreXII =u_form.cleaned_data["scoreXII"]

            diploma = u_form.cleaned_data["diploma"]
            specializationDiploma = u_form.cleaned_data["specializationDiploma"]
            yearOfPassingDiploma = u_form.cleaned_data["yearOfPassingDiploma"]
            scoreDiploma=u_form.cleaned_data["scoreDiploma"]

            UG = u_form.cleaned_data["UG"]
            specializationUG = u_form.cleaned_data["specializationUG"]
            yearOfPassingUG = u_form.cleaned_data["yearOfPassingUG"]
            scoreUG=u_form.cleaned_data["scoreUG"]

            PG = u_form.cleaned_data["PG"]
            specializationPG = u_form.cleaned_data["specializationPG"]
            yearOfPassingPG = u_form.cleaned_data["yearOfPassingPG"]
            scorePG=u_form.cleaned_data["scorePG"]
            EdudetailsModel.objects.get_or_create(user=request.user)

            if not EdudetailsModel.objects.get(user=request.user):
                print(' inserted')
                t=EdudetailsModel(user=request.user,schoolX = schoolX,
                specializationX =specializationX,yearOfPassingX =yearOfPassingX,
                scoreX=scoreX,schoolXII = schoolXII, specializationXII = specializationXII,
                yearOfPassingXII =yearOfPassingXII,scoreXII =scoreXII,diploma = diploma,
                specializationDiploma = specializationDiploma, yearOfPassingDiploma = yearOfPassingDiploma,
                scoreDiploma=scoreDiploma,UG = UG,specializationUG = specializationUG,
                yearOfPassingUG = yearOfPassingUG,scoreUG=scoreUG,PG = PG,
                specializationPG = specializationPG, yearOfPassingPG = yearOfPassingPG,scorePG=scorePG)
                t.save()
                request.user.edudetailsmodel.add(t)
                messages.success(request, f'Your account has been saved!')

            else:
                # Get data from form


                ls.schoolX=request.POST.get("schoolX")
                ls.specializationX=request.POST.get("specializationX")
                ls.yearOfPassingX=request.POST.get("yearOfPassingX")
                ls.scoreX=request.POST.get("scoreX")

                ls.schoolXII=request.POST.get("schoolXII")
                ls.specializationXII=request.POST.get("specializationXII")
                ls.yearOfPassingXII=request.POST.get("yearOfPassingXII")
                ls.scoreXII=request.POST.get("scoreXII")

                ls.diploma=request.POST.get("diploma")
                ls.specializationDiploma=request.POST.get("specializationDiploma")
                ls.yearOfPassingDiploma=request.POST.get("yearOfPassingDiploma")
                ls.scoreDiploma=request.POST.get("scoreDiploma")


                ls.UG=request.POST.get("UG")
                ls.specializationUG=request.POST.get("specializationUG")
                ls.yearOfPassingUG=request.POST.get("yearOfPassingUG")
                ls.scoreUG=request.POST.get("scoreUG")

                ls.PG=request.POST.get("PG")
                ls.specializationPG=request.POST.get("specializationPG")
                ls.yearOfPassingPG=request.POST.get("yearOfPassingPG")
                ls.scorePG=request.POST.get("scorePG")
                ls.save()
                # Update data in Db

                ls.save(update_fields=['schoolX'])
                ls.save(update_fields=['specializationX'])
                ls.save(update_fields=['yearOfPassingX'])
                ls.save(update_fields=['scoreX'])

                ls.save(update_fields=['schoolXII'])
                ls.save(update_fields=['specializationXII'])
                ls.save(update_fields=['yearOfPassingXII'])
                ls.save(update_fields=['scoreXII'])

                ls.save(update_fields=['diploma'])
                ls.save(update_fields=['specializationDiploma'])
                ls.save(update_fields=['yearOfPassingDiploma'])
                ls.save(update_fields=['scoreDiploma'])

                ls.save(update_fields=['UG'])
                ls.save(update_fields=['specializationUG'])
                ls.save(update_fields=['yearOfPassingUG'])
                ls.save(update_fields=['scoreUG'])

                ls.save(update_fields=['PG'])
                ls.save(update_fields=['specializationPG'])
                ls.save(update_fields=['yearOfPassingPG'])
                ls.save(update_fields=['scorePG'])
                messages.success(request, f'Your account has been updated!')
            return redirect('edudetailsView')
        else:
            print (u_form.errors)

    else:
            u_form = EduDetailsUpdateForm()
    context = {
        'u_form': u_form,
        'ls':ls,
        'lst':lst,
        }
    return render(request, 'users/updateedudetails.html', context)

@login_required
def edudetailsView(request):

    edudet=EdudetailsModel.objects.filter(user=request.user)[0]

    return render(request, 'users/edudetailsView.html',{'edudet':edudet})

@login_required
def addskillsset(request):
    skillset=SkillSetDetailsModel.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        skill_form = SkillSetDetailsUpdateForm(request.POST)
        if skill_form.is_valid():
            skillname = skill_form.cleaned_data["skillname"]
            exp = skill_form.cleaned_data["exp"]
            t=SkillSetDetailsModel(user=request.user,skillname = skillname,
            exp =exp)
            t.save()
            request.user.skillsetdetailsmodel.add(t)
            messages.success(request, f'Your skill set has been saved!')
            return redirect('addskillsset')
    else:
        skill_form = SkillSetDetailsUpdateForm()
    context = {
        'skill_form': skill_form,
        'skillset':skillset
        }
    return render(request, 'users/addskillsset.html',context=context)

@login_required
def updateskillsset(request, id):

    skillset=SkillSetDetailsModel.objects.filter(id=id)
    ls=SkillSetDetailsModel.objects.get(id=id)
    if  request.method=='POST':
        skill_form = SkillSetDetailsUpdateForm(request.POST)
        if skill_form.is_valid():
            if skillset:
                ls=SkillSetDetailsModel.objects.get(id=id)
                ls.skillname=request.POST.get("skillname")
                ls.exp=request.POST.get("exp")
                ls.save()
                # Update data in Db
                ls.save(update_fields=['skillname'])
                ls.save(update_fields=['exp'])
                messages.success(request, f'Your Skill set updated Succssfully!')
                return redirect('addskillsset')
        else:
            print("not valid")
    else:
        skill_form = SkillSetDetailsUpdateForm()
    context = {
        'skill_form': skill_form,
        'skillset':skillset,
        'ls':ls
        }
    return render(request, 'users/updateskillset.html',context=context)
