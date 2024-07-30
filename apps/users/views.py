from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserRegisterForm


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm

    def get_context_data(self, **kwargs):
        context = super(
            UserRegisterView, self
        ).get_context_data(**kwargs)

        context['bgimage'] = 'img/пляж.jpg'
        return context