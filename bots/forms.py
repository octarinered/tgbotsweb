from django import forms
from .models import BotAccountModel

class BotAccountCreationForm(forms.ModelForm):
   class Meta:
       model = BotAccountModel
       fields = ['bot_name', ] 

class BotForm(forms.ModelForm):
   class Meta:
       model = BotAccountModel
       fields = ['bot_name', ] 
