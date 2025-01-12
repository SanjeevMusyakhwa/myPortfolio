from django.http import JsonResponse
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number')  # Get phone number
        address = request.POST.get('address')  # Get address

        # Validate required fields
        if not name or not email or not message:
            return JsonResponse({'error': 'Name, email, and message are required.'}, status=400)
        
        # Save data to the database
        contact_entry = ContactMessage(
            name=name,
            email=email,
            message=message,
            phone_number=phone_number,  # Save phone number
            address=address  # Save address
        )
        contact_entry.save()

        return JsonResponse({'message': 'Your message has been received!'}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
