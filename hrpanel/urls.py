from django.urls import path
from . import views
from django.conf.urls import url
from .views import PostListView,PostDetailView,UserPostListView
# PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


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
    path('viewcreatenewjob/<int:jobid>', views.viewcreatenewjob, name='hrpanel-viewcreatenewjob'),
    path('updatecreatenewjob/<int:jobid>', views.updatecreatenewjob, name='hrpanel-updatecreatenewjob'),

    path('post/', PostListView.as_view(), name='hrpanel-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/new', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),




]
