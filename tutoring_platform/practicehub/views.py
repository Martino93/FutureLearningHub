# new_app/views.py
from django.shortcuts import render
from supabase import create_client

import os
import json
from supabase.client import Client
from dotenv import load_dotenv

load_dotenv()

# Replace with your Supabase project URL and public anon key
SUPABASE_URL = os.environ.get("SUPABASE_URL") or ""
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") or ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def quiz_view(request):
    # Fetch the first question from the Supabase table
    response = supabase.table('aqua_rat_train').select('*').limit(1).execute()
    question_data = response.data[0] if response.data else None

    # Check if question_data exists and parse the options column if needed
    if question_data:
        options_val = question_data.get('options')
        if isinstance(options_val, str):
            question_data['options'] = json.loads(options_val)
        else:
            # Already a list or other data structure, no need to parse
            question_data['options'] = options_val

    return render(request, 'practicehub/quiz.html', {'question': question_data})