from django.db import models
from django.contrib.auth import get_user_model
import string
import random

def generate_unique_code():
    length = 6

    while True:
        bot_code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if BotAccountModel.objects.filter(bot_code=bot_code).count() == 0:
            break

    return bot_code

class BotAccountModel(models.Model):
    bot_code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    bot_name = models.CharField(max_length=50, unique=True)

    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.bot_name


        