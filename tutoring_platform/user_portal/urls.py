# filepath: c:\Users\Hamed\Documents\tutoring-platform\FutureLearningHub\tutoring_platform\user_portal\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),  # Example route
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
]
