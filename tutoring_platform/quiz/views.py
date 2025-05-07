import os
import random
from django.shortcuts import render
from django.conf import settings
from supabase import create_client, Client

def math_quiz(request):
    # Connect to Supabase using credentials from settings
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)
    
    # Retrieve the top 5 rows from your table
    response = supabase.table("aqua_rat_train").select("*").limit(5).execute()
    questions = response.data if response.data else []
    
    return render(request, "quiz/math_quiz.html", {"questions": questions})