from django.forms.widgets import FileInput


class HiddenFileInput(FileInput):
    def __init__(self):
        super().__init__()

