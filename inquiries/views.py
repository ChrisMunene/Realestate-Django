from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Inquiry
import realestate.settings as settings

# Create your views here.

def index(request): 
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing_name = request.POST['listing_name']
        name = request.POST['name']
        email = request.POST['email']
        phone= request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing.')
                return redirect('/listings/'+listing_id)

        inquiry = Inquiry(listing_id=listing_id,
        listing_name=listing_name, name=name,
        email=email, phone=phone, message=message, user_id=user_id)

        inquiry.save()

        # Send Email to Realtors. Will add notification and show on dashboard also.
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing_name + '. Sign into the admin panel to view it.',
        #     settings.DEFAULT_FROM_EMAIL,
        #     ['cmk@mailinator.com', 'munenechristoph@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'You request has been submitted. A realtor will contact you shortly.')

        return redirect('/listings/'+listing_id)
