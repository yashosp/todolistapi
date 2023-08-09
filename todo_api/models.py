# from pickle import FALSE
# from django.db import models

# # Create your models here.

# class TodoList(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=255)
#     # status = models.BooleanField(default=FALSE) # Completed or not

#     def __str__(self):
#         return self.title

from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)  # Completed or not

    def __str__(self):
        return self.title
