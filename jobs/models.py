from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create the groups
first_type_group, created = Group.objects.get_or_create(name='FirstType')
second_type_group, created = Group.objects.get_or_create(name='SecondType')

class CustomUser(AbstractUser):

    date_of_birth = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    industry_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    # Add new fields here
    headline = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    date_of_creation = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    
    
class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    content = models.TextField(max_length=2000)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='post_files/', null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)


class JobPost(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
    ]

    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)
    description = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
    is_remote = models.BooleanField(default=None)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    letter_of_motivation = models.TextField(max_length=500)
    applied_on = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    user_account = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    followed_on = models.DateTimeField(auto_now_add=True)
    is_notification_on = models.BooleanField(default=False)


class UserSkill(models.Model):
    user_account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

class University(models.Model):
 
    name = models.CharField(max_length=100)
    headquarter_location = models.CharField(max_length=255, null=True, blank=True)
    branches_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "universities"


class UniversityMajor(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    major = models.ForeignKey('Major', on_delete=models.CASCADE)

class Skill(models.Model):
    name = models.CharField(max_length=100)


class PostEngagement(models.Model):
    CONTENT = 'CT'
    COMMENT = 'CM'
    ENGAGEMENT_TYPE_CHOICES = [
        (CONTENT, 'Content'),
        (COMMENT, 'Comment'),
    ]

    content = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    engagement_type = models.CharField(max_length=2, choices=ENGAGEMENT_TYPE_CHOICES)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Major(models.Model):
    name = models.CharField(max_length=100)


class JobSkill(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


# class Industry(models.Model):
#     name = models.CharField(max_length=100)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    branch_location = models.CharField(max_length=100)
    branch_number = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=2, choices=JobPost.JOB_TYPE_CHOICES)
    company = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='experiences')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    location_type = models.CharField(max_length=2, choices=[('HQ', 'Headquarters'), ('BR', 'Branch')])
    location = models.CharField(max_length=255)
    is_currently_working = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    school = models.ForeignKey('University', on_delete=models.CASCADE)
    degree = models.CharField(max_length=6, choices=[('BS', 'Bachelor'), ('MS', 'Master'), ('PHD', 'PhD')])
    other_degree = models.CharField(max_length=255, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    field_of_study = models.CharField(max_length=255, null=True, blank=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    

