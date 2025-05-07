import random
from django.shortcuts import render

def math_quiz(request):
    # Using a static quiz question as a mock object.
    question = {
        "question": "What is 2 + 2?",
        "answer": "4"
    }
    return render(request, "quiz/math_quiz.html", {"question": question})