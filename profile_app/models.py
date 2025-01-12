from django.db import models

# Create your models here.
class Home(models.Model):
  full_name = models.CharField(max_length=200, verbose_name='Full name')
  typed = models.CharField('typed', max_length=255,help_text="Type Like This -> Designer, Developer, Freelancer, Photographer")
  about_me = models.CharField(max_length=255,verbose_name='Home About me')
  email = models.EmailField("Email Address")
  phone_number = models.CharField(max_length=15)
  facebook = models.URLField("Facebook")
  twitter = models.URLField("Twitter")
  linkedIn = models.URLField("LinkedIn")
  github = models.URLField("Github")
  instagram = models.URLField("Instagram")
  image = models.ImageField('About Profile', upload_to='profile/', blank=False, null=False)
  
  def __str__(self,*args, **kwargs):
    return f"{self.id} {self.full_name}"
