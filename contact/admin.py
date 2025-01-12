from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone_number','address', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message', 'phone_number', 'address')
