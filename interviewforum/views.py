from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from interviewforum.models import Interview,InterviewComments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import InterviewForm,InterviewCommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)


class InterviewDraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    template_name='interviewforum/interview_draft_list.html'
    model=Interview
    paginate_by=2

    context_object_name='interviews'

    def get_queryset(self):
        return Interview.objects.filter(published_date__isnull=True).order_by('create_date')

class InterviewListView(ListView):
    model=Interview
    paginate_by=3
    def get_queryset(self):
        return Interview.objects.filter(published_date__lte=timezone.now())
        #
        # return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class InterviewDetailView(DetailView):
    model=Interview
    paginate_by=3

class CreateInterviewView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='interviewforum/interview_detail.html'
    form_class=InterviewForm
    model=Interview

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)





class InterviewUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='interviewforum/interview_detail.html'
    form_class=InterviewForm
    model=Interview

class InterviewDeleteView(LoginRequiredMixin,DeleteView):
    model=Interview
    success_url=reverse_lazy('interview_list')




##############################################################################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################

@login_required
def add_comment_to_interview_post(request,pk):
    interview=get_object_or_404(Interview,pk=pk)

    if request.method=='POST':
        form=InterviewCommentForm(request.POST)

        if form.is_valid():

            comment=form.save(commit=False)
            comment.interview=interview
            comment.save()
            print('saved')
            return redirect('interview_detail',pk=interview.pk)
    else:
        form=InterviewCommentForm()

    return render(request,'interviewforum/comment_form.html',{'form':form})


@login_required
def interview_comment_approve(request,pk):
    print('approved')
    comment=get_object_or_404(InterviewComments,pk=pk)
    print('approved1')
    comment.approve()
    print(comment.interview.pk)
    return redirect('interview_detail',pk=comment.interview.pk)

@login_required
def interview_comment_remove(request,pk):
    comment=get_object_or_404(InterviewComments,pk=pk)
    post_pk=comment.interview.pk
    comment.delete()
    return redirect('interview_detail',pk=post_pk)

@login_required
def inteview_post_publish(request,pk):
    post=get_object_or_404(Interview,pk=pk)

    post.publish()
    return redirect('interview_detail',pk=pk)
