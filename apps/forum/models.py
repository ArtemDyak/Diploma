from django.db import models
from ..users.models import User


class Message(models.Model):
    text = models.CharField(max_length=512)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)

    attached_file = models.FileField(
        blank=True, default=None, upload_to='forum_messages'
    )
