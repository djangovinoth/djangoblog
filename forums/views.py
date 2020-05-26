from django.shortcuts import render,redirect,reverse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Technical
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

from django.contrib import messages


# Create your views here.




class TechnicalListView(ListView):

    model=Technical

    template_name='forums/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='technicals'
    ordering=['-date_posted']

    paginate_by=5

class UserTechnicalListView(ListView):
    model=Technical

    template_name='forums/user_technicals.html' #<app>/<model>_<viewtype>.html
    context_object_name='technicals'


    paginate_by=5


    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Technical.objects.filter(author=user).order_by('-date_posted')



class TechnicalDetailView(DetailView):
    model=Technical


class TechnicalCreateView(LoginRequiredMixin,CreateView):
    model=Technical

    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)




class TechnicalUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Technical

    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


    def test_func(self):
        technical=self.get_object()
        if self.request.user==technical.author:
            return True
        return False


def addlike(request,pk):
    like=Technical.objects.values('like').filter(pk=pk)[0]
    ls=Technical.objects.get(pk=pk)

    print(like['like'])
    ls.like=like['like']+1

    ls.save()

    ls.save(update_fields=['like'])


    return redirect('technical-detail',pk=pk)

def adddislike(request,pk):
    dislike=Technical.objects.values('dislike').filter(pk=pk)[0]
    ls=Technical.objects.get(pk=pk)

    print(dislike['dislike'])
    ls.dislike=dislike['dislike']+1

    ls.save()

    ls.save(update_fields=['dislike'])


    return redirect('technical-detail',pk=pk)


class TechnicalDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Technical
    success_url='/'
    def test_func(self):
        technical=self.get_object()
        if self.request.user==technical.author:
            return True
        return False
