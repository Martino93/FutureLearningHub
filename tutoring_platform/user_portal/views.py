# filepath: c:\Users\Hamed\Documents\tutoring-platform\FutureLearningHub\tutoring_platform\user_portal\views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .utils import get_supabase_client
import json
from django.db import IntegrityError

# from .models import Pupil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def dashboard(request):
    return render(request, "user_portal/dashboard.html")


@csrf_exempt
def register_user(request):
    if request.method == "GET":
        return render(request, "user_portal/register.html")
    elif request.method == "POST":
        try:
            # Extract data from POST request
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            # registration_code = request.POST.get("registration_code")

            # Validate email
            validate_email(email)

            # Validate password length
            if len(password) < 8:
                return JsonResponse({"error": "Password must be at least 8 characters long"}, status=400)

            # Save the pupil in the database
            user = User.objects.create_user(
                username=email,  # or a different unique identifier
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            return redirect("/user_portal/login/")
        except IntegrityError:
            # Handle unique constraint violation for email
            return render(
                request,
                "user_portal/register.html",
                {"error_message": "An account with this email already exists"},
            )
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == "GET":
        return render(request, "user_portal/login.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Authenticate the user using Django's auth framework (using username as email)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/user_portal/dashboard/")  # redirect to a homepage or user dashboard after login
        else:
            return render(
                request,
                "user_portal/login.html",
                {"error_message": "Invalid email or password"}
            )
    return JsonResponse({"error": "Invalid request method"}, status=405)
