from django.urls import path
from . import views
from django.conf.urls import url

# PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('employeeAddEdudetails/', views.employeeAddEdudetails, name='employeeAddEdudetails'),


    # path('post/new', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),




]
