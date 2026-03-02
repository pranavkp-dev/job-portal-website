from django.http import HttpResponse
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserProfileForm 

from.models import Userreg
from.models import Employerreg
from.models import Jobapplication



def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')


def singleblog(request):
    return render(request,'single-blog.html')


def  contact(request):
    return render(request,'contact.html')


def employerhome(request):
    employers_id = request.session.get('employers_id')

    if not employers_id:
        return redirect('employer')

    jobs = Employerreg.objects.filter(id=employers_id)

    return render(request, 'employer_home.html', {
        'jobs': jobs
    })




def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # ✅ Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        # ✅ Check email (recommended)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
def profile(request):
    profile, created = Userreg.objects.get_or_create(user=request.user)

    return render(request, 'profile.html', {
        'profile': profile
    })




@login_required
def editprofile(request):
    profile, created = Userreg.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'editprofile.html', {'form': form})




def updateprofile(request,id):
    if request.method=="POST":
         
        username = request.POST.get('username')
        email = request.POST.get('email')
        number= request.POST.get('number')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        loc = request.POST.get('loc')
        header = request.POST.get('header')
        bio = request.POST.get('bio')
        qualification = request.POST.get('qualification')
        degree = request.POST.get('degree')
        exp = request.POST.get('exp')
        resume=request.FILES.get('resume')
        
        file_path = None
        if resume:
            file_path = f"uploads/{resume.name}"
            default_storage.save(file_path, ContentFile(resume.read()))

        role = request.POST.get('role')
        type = request.POST.get('type')
        availability = request.POST.get('availability')
        skills = request.POST.get('skills')
        

        edit=Userreg.objects.get(id=id)
        edit.number=number
        edit.dob=dob
        edit.gender=gender
        edit.loc=loc
        edit.header=header
        edit.bio=bio
        edit.qualification=qualification
        edit.degree=degree
        edit.exp=exp
        resume=file_path   
        edit.role=role
        edit.type=type
        edit.availability=availability
        edit.skills=skills

        edit.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile') 











def employer(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        company_desc = request.POST.get('company_desc')
        company_loc = request.POST.get('company_loc')
        company_address = request.POST.get('company_address')
        industry = request.POST.get('industry')
        company_size = request.POST.get('company_size')
        recruiter_name = request.POST.get('recruiter_name')
        recruiter_designation = request.POST.get('recruiter_designation')
        recruiter_email = request.POST.get('recruiter_email')
        recruiter_phone = request.POST.get('recruiter_phone')
        company_logo=request.FILES.get('company_logo')
        
        file_path = None
        if company_logo:
            file_path = f"company_logos/{company_logo.name}"
            default_storage.save(file_path, ContentFile(company_logo.read()))
       
        employers = Employerreg.objects.create(
            company_name=company_name,
            company_desc=company_desc,
            company_loc=company_loc,
            company_address=company_address,
            industry=industry,
            company_size=company_size,
            recruiter_name=recruiter_name,
            recruiter_designation=recruiter_designation,
            recruiter_email=recruiter_email,
            recruiter_phone=recruiter_phone,
            company_logo=file_path,    
        )
        request.session['employers_id'] = employers.id

        return redirect('employerhome') 
    return render(request, 'employer_registration.html')






def addjob(request):
    if request.method == "POST":
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        job_desc= request.POST.get('job_desc')
        company_loc = request.POST.get('company_loc')
        req_skills = request.POST.get('req_skills')
        job_type = request.POST.get('job_type')
        work_mode = request.POST.get('work_mode')
        Exp_level = request.POST.get('Exp_level')
        Education_req = request.POST.get('Education_req')
        salary_range = request.POST.get('salary_range')
        vacancies = request.POST.get('vacancies')
        app_deadline = request.POST.get('app_deadline')
        joining_time = request.POST.get('joining_time')
        recruiter_name = request.POST.get('recruiter_name')
        recruiter_phone = request.POST.get('recruiter_phone')
        recruiter_email = request.POST.get('recruiter_email')
        
       
        addjobs = Employerreg.objects.create(
           job_title=job_title,
           company_name=company_name,
           job_desc=job_desc,
           company_loc=company_loc,
           req_skills=req_skills,
           job_type=job_type,
           work_mode=work_mode,
           Exp_level=Exp_level,
           Education_req=Education_req,
           salary_range=salary_range,
           vacancies=vacancies,
           app_deadline=app_deadline,
           joining_time=joining_time,
           recruiter_name=recruiter_name,
           recruiter_phone=recruiter_phone,
           recruiter_email=recruiter_email,
               
        )
        request.session['addjobs_id'] = addjobs.id

        return redirect('employerhome') 
    return render(request, 'add_jobs.html')



@login_required
def jobs(request):
    jobs = Employerreg.objects.all()

    search = request.GET.get('search')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')

    if search:
        jobs = jobs.filter(job_title__icontains=search)

    if location:
        jobs = jobs.filter(company_loc__icontains=location)

    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)


    return render(request, 'jobs.html', {'data': jobs})




def jobdetails(request,id):

    data={
        'data':Employerreg.objects.get(id=id)
    }

    return render(request,'job_details.html',data)



def jobsedit(request):
    data = {
        "data" : Employerreg.objects.all()

    }
    return render(request,'jobs_edit.html',data)



def delete(request, id):
    dlt = get_object_or_404(Employerreg, id=id)
    dlt.delete()
    messages.success(request, "Job deleted successfully!")
    return redirect('employerhome')   # URL name
 




def edit(request,id):
    data ={
        "des":Employerreg.objects.get(id=id)
    }
    return render(request,'update.html',data)




def update(request,id):
    if request.method=="POST":
         
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        job_desc= request.POST.get('job_desc')
        company_loc = request.POST.get('company_loc')
        req_skills = request.POST.get('req_skills')
        job_type = request.POST.get('job_type')
        work_mode = request.POST.get('work_mode')
        Exp_level = request.POST.get('Exp_level')
        Education_req = request.POST.get('Education_req')
        salary_range = request.POST.get('salary_range')
        vacancies = request.POST.get('vacancies')
        app_deadline = request.POST.get('app_deadline')
        joining_time = request.POST.get('joining_time')
        

        edit=Employerreg.objects.get(id=id)
        edit.company_name=company_name
        edit.job_title=job_title
        edit.job_desc=job_desc
        edit.company_loc=company_loc
        edit.req_skills=req_skills
        edit.job_type=job_type
        edit.work_mode=work_mode
        edit.Exp_level=Exp_level
        edit.Education_req=Education_req
        edit.salary_range=salary_range
        edit.vacancies=vacancies
        edit.app_deadline=app_deadline
        edit.joining_time=joining_time

        edit.save()
        messages.success(request, "Job data updated successfully!")
        return redirect('employerhome') 
        
        

def applyform(request, id):

    job = get_object_or_404(Employerreg, id=id)

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # or register page

    user = get_object_or_404(Userreg, id=user_id)

    if request.method == "POST":
        applicantname = request.POST.get("applicantname")
        applicantemail = request.POST.get("applicantemail")
        applicantnumber = request.POST.get("applicantnumber")

        Jobapplication.objects.create(
            job=job,
            user=user,   # ✅ THIS FIXES ERROR
            applicantname=applicantname,
            applicantemail=applicantemail,
            applicantnumber=applicantnumber
        )

        return HttpResponse(
            '<script>alert("Applied Successfully!"); window.location.href="/jobs/";</script>'
        )

    return render(request, 'apply_form.html', {
        'job': job,
        'user': user
    })


          
           
def employerprofile(request):
    employers_id = request.session.get('employers_id')
    data = {
        'data': Employerreg.objects.get(id=employers_id)
    }
    return render(request, 'employer_profile.html', data)
        


def jobapplications(request):
    data = {
        "application" : Jobapplication.objects.all()

    }
    return render(request,'job_applications.html',data)


def applicant_profile(request, id):

    user = Userreg.objects.get(id=id)

    return render(request, "applicant_profile.html", {
        "user": user
    })