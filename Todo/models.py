from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.CharField(max_length=10, default="False")  # ✅ Fixed


    def __str__(self):
        return self.name
