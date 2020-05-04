from django.shortcuts import render
from .models import Post
from users.models import PermissionModel


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    per=PermissionModel.objects.get(user=request.user)
    print(per)
    print(per.role)
    context={
    'per':per
    }

    if(per.role=="Employer"):
        return render(request, 'hrpanel/home.html', context)    

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
