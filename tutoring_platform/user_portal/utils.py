from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


def get_supabase_client():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    return create_client(supabase_url, supabase_key)
