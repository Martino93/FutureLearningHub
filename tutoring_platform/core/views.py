from django.shortcuts import render
from .models import Tutor, Testimonial


def landing_page(request):
    tutors = Tutor.objects.all()[:3]  # Limit to 3 tutors
    testimonials = Testimonial.objects.all()[:3]  # Limit to 3 testimonials
    return render(
        request,
        "core/landing_page.html",
        {"tutors": tutors, "testimonials": testimonials},
    )


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(
            f"Message from {name}",
            message,
            email,
            ["your-email@example.com"],  # Replace with your email
        )
        return redirect("landing_page")  # Redirect to the landing page after submission
    return render(
        request, "core/contact.html"
    )  # Optional: Render a separate contact page if needed


def services(request):
    return render(request, "core/services.html")


def dashboard(request):
    return render(request, "user_portal/dashboard.html")
