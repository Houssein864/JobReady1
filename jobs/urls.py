from django.urls import path
from .views import login, hello_user, main_page,  signup,create_post
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.login, name='main_page'),
    path('login/', views.login, name='login'),
    path('hello_user/', views.hello_user, name='hello_user'),
    path('main_page/', views.main_page, name='main_page'),
    path('hello_Second/',views.hello_Second,name='hello_Second'),
    path('signup/', views.signup, name='signup'),
    path('signup_second/', views.second_type_signup, name='second_type_signup'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('update_about/', views.update_about, name='update_about'),
    path('update_profile_image/', views.update_profile_image, name='update_profile_image'),
    path('logout/', views.logout_view, name='logout'),
    path('create_job_post/', views.create_job_post, name='create_job_post'),
    path('jobs/', views.all_job_posts, name='job_listing'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
  
    path('add_industry/', views.add_industry, name='add_industry'),
    path('signup_second/', views.signup_second_view, name='signup_second'),
    path('all_jobs/', views.all_jobs_view, name='all_jobs'),   
    path('delete-industry/', views.delete_industry, name='delete_industry'),
    


    path('company_profile/', views.company_profile, name='company_profile'),
    path('get_job_applications/', views.get_job_applications_for_job_post, name='get_job_applications'),
    path('job_post/<int:job_post_id>/', views.job_post_detail, name='job_post_detail'),
    path('search/', views.search, name='search'),

    path('delete_job_post/<int:post_id>/', views.delete_job_post, name='delete_job_post'),
    path('edit_company_profile/', views.edit_company_profile, name='edit_company_profile'),
    

    

    
    
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
