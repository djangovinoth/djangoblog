from django.shortcuts import render
from .models import Post
from users.models import Permission


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    per=Permission.objects.get(user=request.user)
    print(per)
    print(per.Role)
    context={
    'per':per
    }

    if(per.Role=="hr"):
        return render(request, 'hrpanel/home.html', context)

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
