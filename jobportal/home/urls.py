from django.contrib import admin
from django.urls import path , include

from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('contact/', views.contact, name='contact'),
    path('employerhome/', views.employerhome, name='employerhome'),
    path('profile/', views.profile, name='profile'),
    path('employer/',views.employer, name='employer'),
    path('addjob/',views.addjob, name='addjob'),
    path('jobs/',views.jobs, name='jobs'),
    path('jobdetails/<int:id>/', views.jobdetails, name='jobdetails'),
    path('jobsedit/',views.jobsedit, name='jobsedit'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'), 
    path('update/<int:id>',views.update,name='update'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('updateprofile/<int:id>',views.updateprofile,name='updateprofile'),
    path('applyform/<int:id>/', views.applyform, name='applyform'),
    path('employerprofile/', views.employerprofile, name='employerprofile'),
    path('jobapplications/', views.jobapplications, name='jobapplications'),
    path('applicant-profile/<int:id>/', views.applicant_profile, name='applicant_profile'),
    
]