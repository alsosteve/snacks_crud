from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
  # create Snack model

  title = models.CharField(max_length=256)
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=500)
  
  # user friendly display in admin
  def __str__(self):
        return self.name

  def get_absolute_url(self):
        return reverse("thing_detail", args=[str(self.id)])