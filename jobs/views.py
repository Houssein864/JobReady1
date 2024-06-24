from email.headerregistry import Group
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from .forms import CompanyProfileForm
from django.shortcuts import get_object_or_404, redirect

from jobs.forms import PostForm, ProfileImageForm, ProfileUpdateForm, SecondTypeSignUpForm, SignUpForm,JobPostForm,JobApplicationForm
from jobs.models import CustomUser, Industry, Post,JobApplication,JobPost




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
              
                return redirect('main_page')
            elif user.groups.filter(name='FirstType').exists():
                
                return redirect('hello_user')
            elif user.groups.filter(name='SecondType').exists():
               
                return redirect('hello_Second')
            else:
              
                return redirect('default_redirect_page')
        else:
         
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def signup(request): 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='FirstType')
            user.groups.add(group)
            user.save()
       
            industry_name = request.POST.get('industry_name')
            user.industry = industry_name
            user.save()
            auth_login(request, user)
            return redirect('hello_user')
    else:
        form = SignUpForm()
    industries = Industry.objects.all()  
    return render(request, 'signup.html', {'form': form, 'industries': industries})


def second_type_signup(request):
    if request.method == 'POST':
        form = SecondTypeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
         
            group = Group.objects.get(name='SecondType')
           
            user.groups.add(group)
            user.save()
          
            auth_login(request, user)
            return redirect('hello_Second')
    else:
        form = SecondTypeSignUpForm()
    return render(request, 'signup_second.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data['content']
            file = form.cleaned_data['file']
            image = form.cleaned_data['image']
            user = request.user
            post = Post.objects.create(content=content, created_by=user, file=file, image=image)
            return redirect('hello_user')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# def profile(request):
#     posts = Post.objects.filter(created_by=request.user)
#     return render(request, 'profile.html', {'posts': posts, 'user': request.user})

def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if post.created_by == request.user:
            post.delete()
    return redirect('profile')

def update_about(request):
    if request.method == 'POST':
        about = request.POST.get('about')
        request.user.about = about
        request.user.save()
        return redirect('profile')  
    return render(request, 'update_about.html')  




def update_profile_image(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileUpdateForm(instance=request.user)
    industries = Industry.objects.all() 
    return render(request, 'update_profile_image.html', {'form': form, 'industries': industries})

def profile(request):
    posts = Post.objects.filter(created_by=request.user)
    industries = Industry.objects.all()  
    return render(request, 'profile.html', {'posts': posts, 'user': request.user, 'industries': industries})


def logout_view(request):
    logout(request) 
    return redirect('login') 


##ADMIN
def main_page(request):
    industries = Industry.objects.all()  
    first_type_users = CustomUser.objects.filter(groups__name='FirstType')
    second_type_users = CustomUser.objects.filter(groups__name='SecondType')
    
    if request.method == 'POST':
        industry_name = request.POST.get('industry_name')
        Industry.objects.create(name=industry_name)  
        industries = Industry.objects.all() 
    
    return render(request, 'main_page.html', {'industries': industries, 'first_type_users': first_type_users, 'second_type_users': second_type_users})

def add_industry(request):
    if request.method == 'POST':
        industry_name = request.POST.get('industry_name')
        Industry.objects.create(name=industry_name)
        return redirect('main_page')
    return render(request, 'main_page.html')


def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            new_job_post = form.save(commit=False) 
            new_job_post.created_by = request.user 
            new_job_post.save()  
         
    else:
        form = JobPostForm()
           
    return render(request, 'create_job_post.html', {'form': form})
           
            

   




def all_job_posts(request):
  all_jobs = JobPost.objects.all().order_by('created_on')  
  context = {'all_jobs': all_jobs}
  return render(request, 'all_job_posts.html', context)
    
def apply_for_job(request, job_id):
    job = JobPost.objects.get(id=job_id)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job_post = job
            
            application.save()
            return redirect('job_listing')  
    else:
        form = JobApplicationForm()
    
    return render(request, 'all_job_posts.html', {'form': form, 'job': job})


def hello_user(request):
    posts = Post.objects.order_by('-created_on') 
    return render(request, 'hello_user.html', {'posts': posts})

def hello_Second(request):
    posts = Post.objects.order_by('-created_on')  
    return render(request, 'hello_Second.html', {'posts': posts})

def signup_second_view(request):
    
    return render(request, 'signup_second.html')

def all_jobs_view(request):
    
    all_jobs = JobPost.objects.all()
    
 
    return render(request, 'all_job_posts.html', {'all_jobs': all_jobs})


def delete_industry(request):
    if request.method == 'POST':
        industry_id = request.POST.get('industry_id')
        try:
            industry = Industry.objects.get(id=industry_id)
            industry.delete()
        except Industry.DoesNotExist:
            pass  
    return redirect('main_page') 




############################################
@login_required


def company_profile(request):
  
    company = request.user  

    
    company_posts = JobPost.objects.filter(created_by__username__exact=company.username)

   
    context = {'company': company, 'company_posts': company_posts}

    return render(request, 'company_profile.html', context)

    
def get_job_applications_for_job_post(job_post_id):
   
    job_post = get_object_or_404(JobPost, id=job_post_id)

   
    job_applications = JobApplication.objects.filter(job_post=job_post)
    
    context = {
            'job_post': job_post,
            'job_applications': job_applications,
        }

    return render(request, 'company_profile.html', context)
    


def job_post_detail(request, job_post_id):
   
    job_post = get_object_or_404(JobPost, id=job_post_id)

    
    job_applications = JobApplication.objects.filter(job_post=job_post)

    context = {
        'job_post': job_post,
        'job_applications': job_applications,
    }

    return render(request, 'job_post_detail.html', context)





def delete_job_post(request, post_id):
    if request.method == 'POST':
        Job = JobPost.objects.get(id=post_id)
        if Job.created_by == request.user:
            Job.delete()
    return redirect('company_profile')


@login_required 
def edit_company_profile(request):  
    company = request.user  
    
    if request.method == 'POST':  
        form = CompanyProfileForm(request.POST, request.FILES, instance=company)  
        if form.is_valid():  
            form.save() 
            return redirect('company_profile') 
    else: 
        form = CompanyProfileForm(instance=company) 
    
    return render(request, 'edit_company_profile.html', {'form': form})   


def search(request):
    
    query = request.GET.get('q', '').strip()  

   
    matching_users = []
    matching_jobs = []

    if query: 
    
        matching_users = CustomUser.objects.filter(username__icontains=query)

     
        matching_jobs = JobPost.objects.filter(title__icontains=query)

    return render(
        request,
        'search_results.html',
        {
            'users': matching_users,
            'jobs': matching_jobs,
            'query': query,
        },
    )