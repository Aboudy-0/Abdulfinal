
from django.contrib import admin
from django.urls import path
from Hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('department/', views.department, name='department'),
    path('doctors/', views.doctors, name='doctors'),
    path('contacts/', views.contacts, name='contacts'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),

]
