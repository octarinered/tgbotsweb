from django.urls import path
from .views import (
    AllBotsView, 
    AddBotView, 
    ChangeBotView, 
    RemoveBotView, 

    # AboutBotsView
    )

urlpatterns = [    
    path('', AllBotsView.as_view(), name='all_bot_accounts'),
    path('add_new_bot/', AddBotView.as_view(), name='add_new_bot_account'),
    path('change_bot/<int:pk>/', ChangeBotView.as_view(), name='change_bot_account'),
    path('remove_bot/<int:pk>/', RemoveBotView.as_view(), name='remove_bot_account'),

    # path('about_bots', AboutBotsView.as_view(), name='about_bot_accounts'),
]
