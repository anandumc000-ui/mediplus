from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='index'),
    path('Contact', views.contact, name='contact'),
    path('Blog', views.blog, name='blog'),
    path('Service', views.services, name='service'),
    path('About', views.about, name='about'),
    path('Doctor', views.doctor, name='doctor')
]