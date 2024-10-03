from django.views.generic import RedirectView
from django.urls import reverse_lazy


class TitleViewRedirect(RedirectView):
    url = reverse_lazy( 'users_register' )
