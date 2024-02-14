from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .serializers import ContactFormSerializer

def contact_form_view(request):
    if request.method == 'POST':
        serializer = ContactFormSerializer(data=request.POST)
        if serializer.is_valid():
            # Getting validated data
            name = serializer.validated_data['name']
            phone = serializer.validated_data['phone']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            # Preparing email content
            email_subject = 'Contact Form Submission'
            email_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

            # Sending email using Gmail credentials
            send_mail(
                email_subject,
                email_message,
                'spandanbhattarai79@gmail.com',  # Replace with your Gmail email address
                ['spandanbhattarai79@gmail.com'],  # Replace with the recipient's email address
                fail_silently=False,
                auth_user='spandanbhattarai79@gmail.com',  # Replace with your Gmail email address
                auth_password='vwcp cuvj pjss qzdg',  # Replace with the app password you generated
            )

            return JsonResponse({'message': 'Form data sent successfully!'})
    
    return render(request, 'form.html')
