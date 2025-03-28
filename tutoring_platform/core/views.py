from django.shortcuts import render
from .models import Tutor, Testimonial

def landing_page(request):
    tutors = Tutor.objects.all()[:3]  # Limit to 3 tutors
    testimonials = Testimonial.objects.all()[:3]  # Limit to 3 testimonials
    return render(request, 'core/landing_page.html', {
        'tutors': tutors,
        'testimonials': testimonials
    })