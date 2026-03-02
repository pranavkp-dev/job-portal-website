from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Userreg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    number = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    loc = models.CharField(max_length=255, blank=True)
    header = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    qualification = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    exp = models.CharField(max_length=255, blank=True)
    resume = models.ImageField(upload_to='uploads/', blank=True, null=True)
    role = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    availability = models.CharField(max_length=255, blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.username




class Employerreg(models.Model):
    
    company_name=models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to="company_logos/")
    company_desc = models.CharField(max_length=500)
    company_loc=models.CharField(max_length=500)
    company_address=models.CharField(max_length=255)
    industry=models.CharField(max_length=255)
    company_size=models.CharField(max_length=100)
    recruiter_name = models.CharField(max_length=100)
    recruiter_designation = models.CharField(max_length=100)
    recruiter_email = models.EmailField()
    recruiter_phone = models.CharField(max_length=15)
    job_title=models.CharField(max_length=255,default="Not Specified")
    job_desc = models.CharField(max_length=255,default="Not Specified")
    JOB_TYPES = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Contract', 'Contract'),
]

    job_type = models.CharField(max_length=50, choices=JOB_TYPES)

    req_skills = models.CharField(max_length=255,default="Not Specified")
    Exp_level = models.CharField(max_length=255,default="Not Specified")
    Education_req = models.CharField(max_length=255,default="Not Specified")
    salary_range = models.CharField(max_length=255,default="Not Specified")
    salary_type = models.CharField(max_length=255,default="Not Specified")
    vacancies = models.CharField(max_length=255,default="Not Specified")
    app_deadline = models.DateField(default=date.today)
    joining_time = models.CharField(max_length=255,default="Not Specified")
    work_mode = models.CharField(max_length=255,default="Not Specified")
    def __str__(self):
        return f"{self.job_title} - {self.company_name}"



class Jobapplication(models.Model):
    job = models.ForeignKey(Employerreg, on_delete=models.CASCADE)
    user = models.ForeignKey(Userreg, on_delete=models.CASCADE)
    applicantname=models.CharField(max_length=255)
    applicantnumber=models.IntegerField()
    applicantemail=models.EmailField()
    applied_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.applicantname} → {self.job.job_title}"

