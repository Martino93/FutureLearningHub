from django.urls import path
from .views import math_quiz

urlpatterns = [
    path("", math_quiz, name="math_quiz"),
]
