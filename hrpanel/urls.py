from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('hrhome/', views.hrhome, name='hrpanel-hrhome'),
    path('addtechnicalteam/', views.addtechnicalteam, name='hrpanel-addtechnicalteam'),
    path('candidatetracker/', views.candidatetracker, name='hrpanel-candidatetracker'),
    path('createnewjob/', views.createnewjob, name='hrpanel-createnewjob'),
    path('experienceprofile/', views.experienceprofile, name='hrpanel-experienceprofile'),
    path('freshersprofile/', views.freshersprofile, name='hrpanel-freshersprofile'),
    path('mail/', views.mail, name='hrpanel-mail'),
    path('offlineuser/', views.offlineuser, name='hrpanel-offlineuser'),
    path('postjob/', views.postjob, name='hrpanel-postjob'),
    path('shortlisted/', views.shortlisted, name='hrpanel-shortlisted'),
    path('download/<int:id>', views.download, name='hrpanel-download'),
    path('addfreshershortlist/<int:id>', views.addfreshershortlist, name='hrpanel-addfreshershortlist'),





]
