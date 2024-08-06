from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("title_forum")
    next_page = success_url

    def get_context_data(self, **kwargs):
        context = super(
            UserLoginView, self
        ).get_context_data(**kwargs)

        context['bgimage'] = 'img/фон.jpg'
        return context


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_login")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(
            UserRegisterView, self
        ).get_context_data(**kwargs)

        context['bgimage'] = 'img/экран.jpg'
        return context
