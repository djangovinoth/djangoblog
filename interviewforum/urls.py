from . import views
from django.conf.urls import url
from .views import (InterviewListView,InterviewDetailView,CreateInterviewView,
                            InterviewUpdateView,InterviewDeleteView,InterviewDraftListView,add_comment_to_interview_post,
                            interview_comment_approve,interview_comment_remove,inteview_post_publish)


urlpatterns = [
    url(r'interviewquestions',views.InterviewListView.as_view(),name='interview_list'),
    url(r'^interview/(?P<pk>\d+)$',views.InterviewDetailView.as_view(),name='interview_detail'),
    url(r'^interview/new/$',views.CreateInterviewView.as_view(),name='interview_new'),
    url(r'^interview/(?P<pk>\d+)/edit/$',views.InterviewUpdateView.as_view(),name='interview_edit'),
    url(r'^interview/(?P<pk>\d+)/edit/remove/$',views.InterviewDeleteView.as_view(),name='interview_remove'),
    url(r'^drafts/$',views.InterviewDraftListView.as_view(),name='interview_draft_list'),
    url(r'^interview/(?P<pk>\d+)/comment/$',views.add_comment_to_interview_post,name='add_comment_to_interview_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.interview_comment_approve,name='interview_comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.interview_comment_remove,name='interview_comment_remove'),
    url(r'^interview/(?P<pk>\d+)/pubish/$',views.inteview_post_publish,name='inteview_post_publish')


]
