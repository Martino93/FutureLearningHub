from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import get_random_question
from .models import UserQuizAttempt
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

@login_required
def quiz_view(request):
    """
    Displays a new quiz question.
    """
    if 'attempt_id' not in request.session:
        # Start a new quiz attempt
        attempt = UserQuizAttempt.objects.create(user=request.user)
        request.session['attempt_id'] = attempt.id
        request.session['answered_questions'] = []

    answered_questions = request.session.get('answered_questions', [])
    question_data = get_random_question(excluded_ids=answered_questions)

    if not question_data:
        # If no more questions are available, show the results.
        return redirect('quiz_results')

    # Check if options is already a list or dict; otherwise, parse the JSON string.
    options_data = question_data.get('options', '{}')
    if isinstance(options_data, str):
        options = json.loads(options_data)
    else:
        options = options_data

    context = {
        'question': question_data['question'],
        'options': options.items() if isinstance(options, dict) else options,
        'question_id': question_data['id'],
    }
    return render(request, 'practicehub/quiz.html', context)


@login_required
def submit_answer(request):
    """
    Processes the user's answer, provides feedback, and shows a 'Next' button.
    """
    if request.method == 'POST':
        question_id = int(request.POST.get('question_id'))
        selected_option_key = request.POST.get('option')
        print(f"Selected option key: {selected_option_key}")

        # Fetch the correct answer and rationale from Supabase
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        response = supabase.table('aqua_rat_train').select('correct, rationale, options').eq('id', question_id).single().execute()
        question_details = response.data

        # Handle options whether it's a string or already parsed
        options_data = question_details.get('options', '{}')
        if isinstance(options_data, str):
            options = json.loads(options_data)
        else:
            options = options_data
        
        correct_answer_value = question_details['correct']
        print(f"Correct answer value: {correct_answer_value}")
        print(selected_option_key==correct_answer_value)
        
        # Determine if the selected option's value matches the correct answer
        is_correct = selected_option_key==correct_answer_value
        # if isinstance(options, dict):
        #     is_correct = (options.get(selected_option_key) == correct_answer_value)
        # elif isinstance(options, list):
        #     # Assuming the list contains items with index/label pairs or individual values
        #     # Adjust this logic based on your actual data structure
        #     try:
        #         selected_index = int(selected_option_key)
        #         if 0 <= selected_index < len(options):
        #             is_correct = (options[selected_index] == correct_answer_value)
        #     except (ValueError, TypeError):
        #         # Handle case where selected_option_key isn't a valid index
        #         pass
            
        # print(is_correct)

        attempt = UserQuizAttempt.objects.get(id=request.session['attempt_id'])
        if is_correct:
            attempt.score += 1
            attempt.correct_answers += 1
        else:
            attempt.incorrect_answers += 1
        attempt.save()

        # Add the question to the list of answered questions in the session
        answered_questions = request.session.get('answered_questions', [])
        answered_questions.append(question_id)
        request.session['answered_questions'] = answered_questions

        context = {
            'is_correct': is_correct,
            'rationale': question_details['rationale'],
            'correct_answer': correct_answer_value
        }
        return render(request, 'practicehub/answer_feedback.html', context)
    
    return redirect('quiz')


@login_required
def quiz_results(request):
    """
    Displays the final score and clears the session for a new quiz.
    """
    attempt_id = request.session.pop('attempt_id', None)
    request.session.pop('answered_questions', None)

    if attempt_id:
        attempt = UserQuizAttempt.objects.get(id=attempt_id)
        context = {'attempt': attempt}
        return render(request, 'practicehub/results.html', context)

    # If there's no attempt in progress, redirect to start a new quiz
    return redirect('quiz')