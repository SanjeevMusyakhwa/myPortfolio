from django.db import models

# Create your models here.
class About(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  happy_clients = models.BigIntegerField(default=0)
  experience_year = models.BigIntegerField(default=0)
  projects_completed = models.BigIntegerField(default=0)
  image = models.ImageField("About Image", upload_to='about/', blank=False, null=False)
  
  def __str__(self, *args, **kwargs):
    return f"{self.id} {self.title}"
