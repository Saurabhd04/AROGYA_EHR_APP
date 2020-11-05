from django.db import models

# Create your models here.

class Personal_info(models.Model):
    name = models.CharField(max_length = 100, blank = True, default = "")
    message = models.TextField()