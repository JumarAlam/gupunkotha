from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):

    message = models.TextField()

    to = models.ForeignKey(
        to=get_user_model()
    )

    on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.message
