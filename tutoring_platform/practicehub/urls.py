# new_app/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('quiz/', views.quiz_view, name='quiz'),
]