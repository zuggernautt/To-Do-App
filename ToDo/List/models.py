from django.db import models

class Task(models.Model):
    TaskInfo = models.CharField(max_length=50,
    help_text = 'Enter the task details in brief')

    def __str__(self):
        return self.TaskInfo



