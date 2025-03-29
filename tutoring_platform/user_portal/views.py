# filepath: c:\Users\Hamed\Documents\tutoring-platform\FutureLearningHub\tutoring_platform\user_portal\views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_supabase_client
import json


def dashboard(request):
    return render(request, "user_portal/dashboard.html")


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        registration_code = data.get("registration_code")

        supabase = get_supabase_client()

        # Check if the registration code is valid
        response = (
            supabase.table("registration_codes")
            .select("*")
            .eq("code", registration_code)
            .eq("is_used", False)
            .execute()
        )
        if not response.data:
            return JsonResponse(
                {"error": "Invalid or already used registration code"}, status=400
            )

        # Register the user in Supabase Auth
        auth_response = supabase.auth.sign_up(
            {"email": email, "password": password},
            {"data": {"role": "student"}},  # Add role metadata
        )
        if "error" in auth_response:
            return JsonResponse(
                {"error": auth_response["error"]["message"]}, status=400
            )

        # Mark the registration code as used
        supabase.table("registration_codes").update({"is_used": True}).eq(
            "code", registration_code
        ).execute()

        return JsonResponse({"message": "User registered successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        supabase = get_supabase_client()

        # Authenticate the user
        auth_response = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
        if "error" in auth_response:
            return JsonResponse(
                {"error": auth_response["error"]["message"]}, status=400
            )

        return JsonResponse(
            {"message": "Login successful", "session": auth_response["session"]}
        )
    return JsonResponse({"error": "Invalid request method"}, status=405)
