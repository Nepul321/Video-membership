from django.shortcuts import (
        redirect, 
        render,
)

from django.contrib.auth import (
    login, 
    logout
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
        AuthenticationForm
)

from django.contrib.auth.models import (
    User
)

from .models import (
    UserKey
)

from src.settings import EMAIL_HOST_USER

from django.core.mail import send_mail

from .decorators import (
    unauthenticated_user,
    not_active_user
)

from .forms import (
    SignUpForm
)

current_host = "http://localhost:8000"

@unauthenticated_user
def LoginView(request):
    template = "auth/login.html"
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
       'form' : form,
    }
    return render(request, template, context)

@login_required
def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('accounts-login')
    else:
        return redirect('home')

@unauthenticated_user
def SignUpView(request):
    template = "auth/registration/signup.html"
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        email = request.POST['email']
        qs = User.objects.filter(email=email)
        if form.is_valid() and not qs:
            form.save()
            qs = User.objects.filter(username=request.POST['username'])
            user = qs.first()
            user_key = UserKey.objects.create(
                user=user
            )
            user_key.save()
            user.is_active = False
            user.save()
            subject = "Verify your email"
            message = f"Thanks for signing up. \n Verify your email - {current_host}/accounts/activate-account/{user_key.key}/"
            email_from = EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            template2 = "auth/accounts/email_sent.html"
            context2 = {

            }

            return render(request, template2, context2)


    context = {
       'form' :  form,
    }

    return render(request, template, context)

@not_active_user
def ActivateAccountView(request, token):
        try:
            user = UserKey.objects.get(key=token)
            if user.activated == False:
                user.activated = True
                user.save()
                user.user.is_active = True
                user.user.save()
                # profile = Profile.objects.create(
                #     user=user
                # )
                # profile.save()
            else:
                return redirect('/')
        except:
            return redirect('/')
        template = 'auth/accounts/email_verified.html'
        context = {}
        return render(request, template, context)