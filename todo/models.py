from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) #optional 
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # specific date and time. anytime a new "todo" object is created it will be givien the value automaticaly  
    completed = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self): #so that the title appears as the name of the todo object in the admin page
        return self.title
