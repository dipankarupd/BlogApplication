from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    abstract = models.TextField()
    description = models.TextField()
    image_url = models.URLField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timeOfPosting = models.DateTimeField(auto_now_add=True)
