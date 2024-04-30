from django.db import models
from django.contrib.auth.models import User
# juliette putasse1$
# bernard numeric1$

class Task(models.Model):  # Define a Task class which is a database model
    user = models.ForeignKey(  # ForeignKey field linking each task to a user
        'auth.User',  # User model provided by Django to manage users
        on_delete=models.CASCADE,  # If the user is deleted, also delete associated tasks
        null=True,  # Allow NULL value in the database
        blank=True  # Allow the field to be left empty in forms
    )
    title = models.CharField(max_length=200)  # Short text field for the task title
    description = models.TextField(null=True, blank=True)  # Long text field for task description
    complete = models.BooleanField(default=False)  # Boolean field to indicate if the task is complete or not
    created = models.DateTimeField(auto_now_add=True)  # Automatic creation date and time field
    
    def __str__(self):  # Special method to represent the object as a string
        return self.title  # Return the task title as the object representation
    
    class Meta:  # Class for additional model metadata
        ordering = ['complete']  # Define the default order of tasks returned by the database
                                 # here, incomplete tasks will be returned first
