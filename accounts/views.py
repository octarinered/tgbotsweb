from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class UserProfileView(generic.DetailView):
    model = get_user_model()
    template_name = 'account/user_profile.html'

    # def get_context_data(self, *args, **kwargs):
    #     users = Profile.objects.all()
    #     context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
    #     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    #     context['page_user'] = page_user
    #     return context