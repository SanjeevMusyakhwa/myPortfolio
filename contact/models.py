from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number field (optional)
    address = models.TextField(blank=True, null=True)  # Address field (optional)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
