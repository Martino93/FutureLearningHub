# filepath: c:\Users\Hamed\Documents\tutoring-platform\FutureLearningHub\tutoring_platform\user_portal\views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .utils import get_supabase_client
import json

from .models import Pupil


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
            registration_code = request.POST.get("registration_code")

            # Validate email
            validate_email(email)

            # Validate password length
            if len(password) < 8:
                return JsonResponse({"error": "Password must be at least 8 characters long"}, status=400)

            # Save the pupil in the database
            Pupil.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                registration_code=registration_code,
            )

            return redirect("/user_portal/login/")
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
        try:
            # Extract data from POST request
            email = request.POST.get("email")
            password = request.POST.get("password")

            supabase = get_supabase_client()

            # Authenticate the user
            auth_response = supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            if "error" in auth_response:
                return JsonResponse(
                    {"error": auth_response["error"]["message"]}, status=400
                )

            # Redirect to the dashboard on successful login
            return redirect("/user_portal/dashboard/")
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)
