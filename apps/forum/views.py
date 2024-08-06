from django.views.generic import TemplateView
from django.urls import reverse_lazy


class ForumTitleView(TemplateView):
    template_name = "forum/title.html"

    def get_context_data(self, **kwargs):
        context = super(
            ForumTitleView, self
        ).get_context_data(**kwargs)

        context['bgimage'] = 'img/фон.jpg'
        return context


