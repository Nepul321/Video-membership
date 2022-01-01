from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    SignUpView,
    ActivateAccountView,
    AccountView,
    PasswordView,
    DeleteAccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('sign-up/', SignUpView, name="signup"),
    path('activate-account/<token>/', ActivateAccountView, name="activate"),
    path('account/', AccountView, name="account"),
    path('password/', PasswordView, name="password"),
    path('delete/', DeleteAccountView, name="delete"),
]
