from django.urls import path, include
from .views import SignupPageView, UserProfileView

urlpatterns = [
    path('', include('allauth.urls')),
    path('signup/', SignupPageView.as_view(), name='signup'),

    path('user/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]