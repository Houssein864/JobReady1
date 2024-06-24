from django.contrib import admin
from .models import CustomUser, Industry,Post,JobPost,JobApplication

admin.site.register(CustomUser)
admin.site.register(Industry)
admin.site.register(Post)
admin.site.register(JobPost)
admin.site.register(JobApplication)






