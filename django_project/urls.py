"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('edudetails/', user_views.edudetails, name='edudetails'),
    path('edudetailsView/', user_views.edudetailsView, name='edudetailsView'),
    path('updateedudetails/', user_views.updateedudetails, name='updateedudetails'),

    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('addcompanyView/', user_views.addcompanyView, name='addcompanyView'),
    path("deletecompany/<int:id>",user_views.deletecompany,name='deletecompany'),
    path("updatecompany/<int:id>",user_views.updatecompany,name='updatecompany'),
    path('addpersonaldetails/', user_views.addpersonaldetails, name='addpersonaldetails'),
    path('personaldetailsView/', user_views.personaldetailsView, name='personaldetailsView'),
    path('updatepersonaldetails/', user_views.updatepersonaldetails, name='updatepersonaldetails'),
    path('addskillsset', user_views.addskillsset, name='addskillsset'),
    path('deleteskillset/<int:id>', user_views.deleteskillset, name='deleteskillset'),


    path('updateskillsset/<int:id>', user_views.updateskillsset, name='updateskillsset'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('employeelogin/', auth_views.LoginView.as_view(template_name='users/employeelogin.html'), name='employeelogin'),
    path('employerlogin/', auth_views.LoginView.as_view(template_name='users/employerlogin.html'), name='employerlogin'),
    path('employeeregister/', user_views.employeeregister, name='employeeregister'),
    path('companycode/', user_views.companycode, name='companycode'),
    path('hrregister/', user_views.hrregister, name='hrregister'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    path('', include('hrpanel.urls')),
    path('', include('employee.urls')),
    path('', include('forums.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
