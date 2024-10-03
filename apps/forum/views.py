from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from . models import Message
from .forms import NewMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ForumTitleView(TemplateView):
    template_name = "forum/title.html"

    def get_context_data(self, **kwargs):
        context = super(
            ForumTitleView, self
        ).get_context_data(**kwargs)

        context["messages"] = Message.objects.all()
        context['bgimage'] = 'img/ддд.avif'
        return context


class MessageCreateView(LoginRequiredMixin, FormView):
    template_name = "forum/new_message.html"
    form_class = NewMessageForm
    success_url = reverse_lazy('title_forum')

    def form_valid(self, form):
        msg = form.save(commit=False)
        msg.sender = self.request.user
        msg.save()
        return super().form_valid(form)


