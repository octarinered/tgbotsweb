from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Я пока не придумал зачем, но мне может пригодиться
    # возможность расширения модели - это можно делать тут:
    # bio = models.TextField(max_length=500, blank=True)

    pass

    def __str__(self):
        return self.username