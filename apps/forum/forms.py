from django.forms import ModelForm
from .models import Message


class NewMessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('id', )
