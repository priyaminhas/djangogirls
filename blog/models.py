from django.db import models
from django.utils import timezone


#define model with name post
# models.Model means post is django model so django knows that it will be saved in database
class Post(models.Model):
	#defining properties
    author = models.ForeignKey('auth.User') #link to other model
    title = models.CharField(max_length=200)  #text with limited number of characters
    text = models.TextField() #text with no limit
    created_date = models.DateTimeField(
            default=timezone.now) #this is the date and time
    published_date = models.DateTimeField(
            blank=True, null=True)
	#function definition 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
