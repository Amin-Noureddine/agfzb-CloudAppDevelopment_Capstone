from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    context = {}
    if request.method == "GET":
        # You can add any context data needed for the about page
        return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    if request.method == "GET":
        # You can add any context data needed for the contact page
        return render(request, 'djangoapp/contact.html', context)
# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']  # Corrected field name to 'password'
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/user_login.html', context)
    else:
        return render(request, 'djangoapp/user_login.html', context)
# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:index')
# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/user_registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.debug("{} is new user".format(username))
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/user_registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        # You can fetch dealer details and reviews for the specified dealer_id here
        # Replace the following with your logic to get dealer details and reviews
        dealer_details = {}  # Replace with your code to fetch dealer details
        reviews = []  # Replace with your code to fetch reviews

        context = {
            "dealer_details": dealer_details,
            "reviews": reviews,
        }

        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_review(request, dealer_id):
    if request.method == "POST":
        # Check if the user is authenticated
        if request.user.is_authenticated:
            form = request.POST
            review = {}  # Create an empty dictionary for the review data

            # Populate the review data dictionary based on form inputs
            review["name"] = f"{request.user.first_name} {request.user.last_name}"
            review["dealership"] = dealer_id
            review["review"] = form["content"]

            # Check if the user made a purchase
            if form.get("purchasecheck"):
                review["purchase"] = True
                purchase_date_str = form.get("purchasedate")
                if purchase_date_str:
                    review["purchase_date"] = datetime.strptime(purchase_date_str, "%m/%d/%Y").isoformat()
                else:
                    review["purchase_date"] = None
            else:
                review["purchase"] = False
                review["purchase_date"] = None

            # You can continue populating the review dictionary with other relevant fields

            # After populating the review data, you can save it to your database or perform any other required actions
            # Example: Save the review to the database

            # Redirect the user to the dealer details page after submitting the review
            return redirect('djangoapp:get_dealer_details', dealer_id=dealer_id)
        else:
            # If the user is not authenticated, you can redirect them to the login page or take appropriate action
            # Redirect to the login page
            return redirect('djangoapp:login')
    else:
        # Handle GET request or other cases as needed
        # Render the add_review form or take appropriate action
        # Example: Render the form for adding a review
        context = {}
        return render(request, 'djangoapp/add_review.html', context)
