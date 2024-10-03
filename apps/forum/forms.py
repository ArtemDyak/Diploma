from django.forms import ModelForm
from django import forms
from .models import Message


class NewMessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('id', 'sender')

        widgets = {
            'file': forms.widgets.FileInput()
        }

        labels = {
            'content': 'Содержание',
            'attached_file': 'Прикрепить файл'
        }
