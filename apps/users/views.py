from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserRegisterForm


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserRegisterView(FormView):
    template_name = "user/register.html"
    form_class = UserRegisterForm

