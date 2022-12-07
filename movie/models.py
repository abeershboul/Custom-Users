from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

# Create your models here.
from django.urls import reverse
class Movie (models.Model):
  title = models.CharField(max_length=64)
  purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  description = models.TextField(default='')
  img_url=models.TextField(default='NO image available!')

  def __str__(self):
    return self.title

   

