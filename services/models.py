from django.db import models

# Create your models here.
class Service(models.Model):
  icon_class = models.CharField("Service Icon Class", max_length=100, blank=True, null=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
    
  def __str__(self, *args, **kwargs):
    return f"{self.id} {self.title}"

