from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jobs.models import CustomUser, Industry, Post, JobApplication,JobPost
 

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'date_of_birth', 'full_name', 'gender', 'email', 'phone', 'industry_name')

class SecondTypeSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='', label='Email')
    location = forms.CharField(max_length=100, required=False, help_text='', label='Location')
    industry_name = forms.ModelChoiceField(queryset=Industry.objects.all(), empty_label="Select Industry", label='Industry Name')
    phone = forms.CharField(max_length=15, help_text='', label='Phone')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'location', 'industry_name', 'phone')

    def __init__(self, *args, **kwargs):
        super(SecondTypeSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'file', 'image']


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'email', 'phone', 'industry_name', 'about']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'email', 'phone', 'industry_name', 'about']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['industry_name'].widget = forms.Select(choices=Industry.objects.all().values_list('name', 'name'))


class JobPostForm(forms.ModelForm):
  class Meta:
    model = JobPost
    fields = ['title', 'job_type', 'description', 'is_active', 'is_remote', # ... other relevant fields ...
              ]

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['letter_of_motivation']
        widgets = {
            'letter_of_motivation': forms.Textarea(attrs={'rows': 5}),
        }




class CompanyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'email', 'phone', 'industry_name', 'about']

    def _init_(self, *args, **kwargs):
        super(CompanyProfileUpdateForm, self)._init_(*args, **kwargs)
        self.fields['industry_name'].widget = forms.Select(choices=Industry.objects.all().values_list('name', 'name'))




class CompanyProfileForm(forms.ModelForm):  # Define a form class for company profile editing, inheriting from forms.ModelForm

    class Meta:  # Meta class to provide additional information about the form
        model = CustomUser  # Specify the model to be used for the form
        fields = ['full_name', 'profile_image', 'industry_name', 'about']  # Define the fields to be included in the form
        widgets = {  # Define widgets for form fields (e.g., HTML input types)
            'profile_image': forms.ClearableFileInput(), 
        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
    filter_by = forms.ChoiceField(label='Filter by', choices=[('users', 'Users'), ('companies', 'Companies')])



