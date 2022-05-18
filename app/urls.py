from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_list, name='jobs_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/new/', views.job_new, name='job_new'),
]