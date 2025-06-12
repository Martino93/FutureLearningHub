# from django.conf import settings
import os
from supabase import create_client
import random
from dotenv import load_dotenv
from supabase.client import Client

load_dotenv()

# Replace with your Supabase project URL and public anon key
SUPABASE_URL = os.environ.get("SUPABASE_URL") or ""
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") or ""

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_random_question(excluded_ids=[]):
    """
    Fetches a random question from the Supabase table, excluding any IDs that have already been answered in the current session.
    """
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # This is not the most performant way for very large tables.
    # A better approach would be to get a count and select a random offset.
    query = supabase.table('aqua_rat_train').select('id, question, options').execute()
    
    available_questions = [q for q in query.data if q['id'] not in excluded_ids]
    print(f"Available questions: {len(available_questions)}")
    
    if not available_questions:
        return None
        
    return random.choice(available_questions)