from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    SignUpView,
    ActivateAccountView,
    AccountView
)

urlpatterns = [
    path('login/', LoginView, name="accounts-login"),
    path('logout/', LogoutView, name="accounts-logout"),
    path('sign-up/', SignUpView, name="signup"),
    path('activate-account/<token>/', ActivateAccountView, name="activate"),
    path('account/', AccountView, name="account"),
]
