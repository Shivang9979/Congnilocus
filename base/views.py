from base.models import CustomUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import logging
import random
from .models import QuizQuestion, Job
from .Algo import algo

random_questions = {
    'Artistic': [],
    'Conventional': [],
    'Enterprising': [],
    'Investigative': [],
    'Realistic': [],
    'Social': []
}


log_of_loging = logging.getLogger(__name__)
log_of_loging.setLevel(logging.INFO)

def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def loginPage(request):
    page='Login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        if 'Login' in request.POST:
            email=request.POST.get('email')
            password=request.POST.get('password')
            try:
                email=CustomUser.objects.get(email=email)
                
            except:
                messages.error(request,'Email not exist')
                log_of_loging.info(f'Invalid user {email} try to Login')
            else:
                user=authenticate(request,email=email,password=password)
                if user is not None:
                    login(request,user)
                    log_of_loging.info(f'{email} has Logged in')
                    return redirect('index')
                else:
                    messages.error(request, 'Invalid password')
                    messages.error(request,'Please enter right password')
                    log_of_loging.error(f'{email} has enter wrong password')
        if 'Registration' in request.POST:
              password=request.POST.get('password')
              confirmPassword=request.POST.get('confirmPassword')
              print(request.POST)
              if password==confirmPassword:
               
                try:
                    CustomUser.objects.create_user(
                        username=request.POST.get('username'),
                        email=request.POST.get('email'),
                        password=request.POST.get('password'),
                        gender=request.POST.get('gender'),
                        birthdate=request.POST.get('birthdate')
                    )
                except:
                    messages.error(request,'Email already exist')
                    messages.error(request,'Please try to signup with different email id')
                    log_of_loging(f'{email} already exist')
            
              else:
                  messages.error(request,'Password does not match')
                  return redirect(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    log_of_loging.info(f'{request.user} has Logged out')
    logout(request)
    return redirect('index')

@login_required(login_url="login")
def get_questions(request):
    # Initialize dictionaries to store random questions for each factor

    factor_name_to_code = {
        'Artistic': 'a',
        'Conventional': 'c',
        'Enterprising': 'e',
        'Investigative': 'i',
        'Realistic': 'r',
        'Social': 's',
    }

    # Define the number of questions to retrieve for each factor
    num_questions_per_factor = 5

    # Loop through each factor and retrieve random questions
    for factor_name, factor_code in factor_name_to_code.items():

        # Use Django's QuerySet and random module to retrieve random questions
        factor_questions = QuizQuestion.objects.filter(primaryfact=factor_code)

        random_questions[factor_name] = random.sample(
            list(factor_questions), num_questions_per_factor)

    # Organize and pass the questions in the template
    context = {'random_questions': random_questions}
    return render(request, 'quiz.html', context)

@login_required(login_url="login")
def process_user_input(request):
    current_quiz_questions = []
    rating_list = []
    if request.method == 'POST':
        question_ratings = {}
        for factor_name, questions in random_questions.items():
            for question in questions:

                # current_quiz_questions.append(question)
                question_id = question.Q_id
                rating = request.POST.get(f'question_rating_{question_id}')
                rating_list.append(rating)
                # print(f'Question {question_id} Rating: {rating}')
                question_data = {
                    'Q_id': question.Q_id,
                    'Question': question.Question,
                    'primaryfact': question.primaryfact,
                    'otherfact': question.otherfact,
                }
                current_quiz_questions.append(question_data)

        print(rating_list)
        suggestion = algo(current_quiz_questions, rating_list)
        # print(suggestion)
        # Now you have a dictionary with question IDs as keys and their ratings as values
        return render(request, 'result.html', {'suggestion': suggestion})

        # return redirect('get_questions')
# def process_user_input(request):
#     if request.method == 'POST':
#         question_ratings = {}
#         for factor_name, questions in random_questions.items():
#             for question in questions:
#                 print(question.Q_id)
#         print(request.POST.get('question_rating'))

#         # Now you have a dictionary with question IDs as keys and their ratings and factors as values


#         return redirect('get_questions')


# def process_user_input(request):
#     if request.method == 'POST':
#         question_ids = []
#         question_ratings = {}
#         factor = None

#         for key, value in request.POST.items():
#             if key.startswith('question_id_'):
#                 # Extract question IDs
#                 question_ids.append(value)
#             elif key.startswith('question_rating_'):
#                 # Use the question ID as the key and the rating as the value
#                 question_ratings[key.replace('question_rating_', '')] = value
#             elif key == 'factor':
#                 # Assuming you have a hidden input field for the factor
#                 factor = value

#         # Now you have the factor, a list of question IDs, and a dictionary of question ratings
#         print("Factor:", factor)
#         print("Question IDs:", question_ids)
#         print("Question Ratings:", question_ratings)

#         return redirect('get_questions')
