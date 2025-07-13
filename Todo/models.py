from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    completed = models.CharField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
