from django.urls import path
from . import views
from .views import (TechnicalListView,UserTechnicalListView,
                    TechnicalDetailView,TechnicalCreateView,
                    TechnicalUpdateView,TechnicalDeleteView)


urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('technical/', TechnicalListView.as_view(), name='technical-home'), #<app>/<model>_<viewtype>.html
    path('technical/<int:pk>/', TechnicalDetailView.as_view(), name='technical-detail'),
    path('user/<str:username>', UserTechnicalListView.as_view(), name='user-technicals'),
    path('technical/new', TechnicalCreateView.as_view(), name='technical-create'),
    path('technical/<int:pk>/update', TechnicalUpdateView.as_view(), name='technical-update'),
    path('technical/<int:pk>/delete', TechnicalDeleteView.as_view(), name='technical-delete'),
    path('addlike/<int:pk>/update', views.addlike, name='technical-addlike'),
    path('adddislike/<int:pk>/update', views.adddislike, name='technical-adddislike'),




]
