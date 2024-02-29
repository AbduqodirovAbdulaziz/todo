from django.db import models
from  django.contrib.auth.models import User

class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks')
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=30,choices=(
        ('Not started','Not started'),
        ('In progress','In progress'),
        ('Completed','Completed'),
    ))
    created_at=models.DateField(auto_now_add=True)
    deadline=models.DateField()

    def __str__(self):
        return f"{self.user}: {self.title}"

