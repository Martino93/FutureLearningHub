# new_app/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.quiz_view, name='quiz_view'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('results/', views.quiz_results, name='quiz_results'),
]