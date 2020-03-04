from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from simple_email_confirmation.models import EmailAddress

from accounts.forms import SignUpForm


def index(request):

    # Render the HTML template base.html with the data in the context variable
    return render(request, 'index.html', context={})


def about(request):

    # Render the HTML template base.html with the data in the context variable
    return render(request, 'about.html', context={})


def account_confirmation(request, confirmation_key):
    # Fixme: Exception handling.
    simple = EmailAddress.objects.get(key=confirmation_key)
    simple.user.confirm_email(confirmation_key)
    return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(Q(username=username) | Q(email=username))
        username = user.username
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('Login done.')
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            simple = EmailAddress.objects.get(user=user)
            print(simple.key)
            message = request.META['HTTP_HOST'] + '/confirma-email/' + simple.key + '/'
            send_mail('Activate Account', 'Use %s to confirm your email' % message, 'srivastava.sparsh@gmail.com', [user.email])
            res = "Email has been sent to your mail. Please confirm and <a href='/login/'>login</a>"
            return HttpResponse(res)
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})