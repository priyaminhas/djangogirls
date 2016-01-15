from django.contrib import admin
from .models import Post #importing the model post

admin.site.register(Post) #to make model visible to the admin page need to register 
