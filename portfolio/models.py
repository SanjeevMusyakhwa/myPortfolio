from django.db import models


class Protfolio(models.Model):
    short_description = models.CharField('Short Description', max_length=195)
    title = models.CharField(max_length=100)
    image = models.ImageField('Protfolio Image', upload_to='protfolio/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.id} {self.title}"
