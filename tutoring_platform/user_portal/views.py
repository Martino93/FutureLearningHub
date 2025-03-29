# filepath: c:\Users\Hamed\Documents\tutoring-platform\FutureLearningHub\tutoring_platform\user_portal\views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'user_portal/dashboard.html')