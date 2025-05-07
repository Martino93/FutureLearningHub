import json
from supabase import create_client, Client
import os

# Replace with your Supabase project URL and public anon key
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Replace with the path to your JSON Lines file
json_file_path = "./load_data/aqua_rat_train.json"

try:
    print(f"Reading data from {json_file_path}...")

    problems_to_insert = []
    # Read the JSON Lines file line by line
    with open(json_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip() # Remove leading/trailing whitespace
            if not line:
                continue # Skip empty lines

            try:
                # Parse each line as a JSON object
                item = json.loads(line)

                # Prepare data for insertion
                problems_to_insert.append({
                    "question": item.get("question"),
                    "options": item.get("options"), # This should map directly to your JSONB column
                    "rationale": item.get("rationale"),
                    "correct": item.get("correct")
                })
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line}. Error: {e}")
                # Decide whether to skip the line or handle the error
                continue
            except Exception as e:
                print(f"An error occurred processing line: {line}. Error: {e}")
                continue

    if problems_to_insert:
        print(f"Prepared {len(problems_to_insert)} problems for insertion.")

        # Insert data in batches
        batch_size = 500 # You can adjust the batch size based on performance
        for i in range(0, len(problems_to_insert), batch_size):
            batch = problems_to_insert[i:i + batch_size]
            print(f"Inserting batch {int(i/batch_size) + 1} of {len(problems_to_insert) // batch_size + (1 if len(problems_to_insert) % batch_size > 0 else 0)}...")
            try:
                # Use the execute() method with the data
                response = supabase.table("aqua_rat_train").insert(batch).execute()

                # Check for errors in the response
                if response.get("error"):
                    print(f"Error inserting batch starting at index {i}: {response['error']}")
                # You might want to check response.data for successfully inserted rows if needed
                # else:
                #     print(f"Successfully inserted batch starting at index {i}.")

            except Exception as e:
                 print(f"An error occurred during insertion of batch starting at index {i}: {e}")


        print("Data upload process finished.")
    else:
        print("No valid problems found in the JSON Lines file to insert.")

except FileNotFoundError:
    print(f"Error: JSON file not found at {json_file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")