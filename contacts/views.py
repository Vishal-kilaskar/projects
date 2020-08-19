from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

def contacts(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, 'You have already made an query for this listing !')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for '+ listing + 'please view it from admin panel',
            EMAIL_HOST_USER,
            [realtor_email],
            fail_silently=False
        )
        messages.success(request, 'Your query has been submitted a realtor will get back to you soon !')
        return redirect('/listings/'+listing_id)
