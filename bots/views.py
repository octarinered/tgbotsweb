from django.urls import reverse_lazy
from django.views import generic

from .models import BotAccountModel
from .forms import BotForm
from django.contrib.auth import get_user_model

class AllBotsView(generic.ListView):
    model = BotAccountModel
    form_class = BotForm
    template_name = 'bots/bots.html'

class AddBotView(generic.CreateView):
    model = BotAccountModel
    form_class = BotForm
    template_name = 'bots/add_new_bot.html'
    success_url = reverse_lazy('all_bot_accounts')

class ChangeBotView(generic.UpdateView):
    model = BotAccountModel
    form_class = BotForm
    template_name = 'bots/change_bot.html'
    success_url = reverse_lazy('all_bot_accounts')

class RemoveBotView(generic.DeleteView):
    model = BotAccountModel
    form_class = BotForm
    template_name = 'bots/remove_bot.html'
    success_url = reverse_lazy('all_bot_accounts')