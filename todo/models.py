from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100) #this make a charfield in the table inside the database
    is_done = models.BooleanField(default=False) # similary creates a boolean field
    created_at = models.DateTimeField(auto_now_add=True) # the time and date of creation of the object
    updated_at = models.DateTimeField(auto_now=True) # the time and date of latest update of the odject

    def __str__(self):
        return self.task
