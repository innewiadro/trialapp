from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import SignUpForm, CustomUserChangeForm, ProfileForm, CustomPasswordChangeForm
from .models import Profile
from django.contrib.auth.mixins import PermissionRequiredMixin

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('index')


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy("index")


class CustomLoginView(LoginView):
    template_name = 'login.html'


class UserListView(ListView):
    template_name = "users.html"
    queryset = Profile.objects.all()


class BiographyView(DetailView):
    model = Profile
    template_name = "user_detail.html"
    context_object_name = "profile"


class UserUpdateView(UpdateView):
    template_name= "user_edit.html"
    
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("users-list")

    def get_object(self, queryset=None):
        return Profile.objects.get(pk=self.kwargs["pk"]).user


class ContactUptadeView(UpdateView):
    model = Profile
    success_url = reverse_lazy("users-list")
    form_class = ProfileForm
    template_name= "contact_edit.html"
    
class ProfileDeleteView(DeleteView):
    template_name = "user_delete.html"
    model = Profile
    success_url = reverse_lazy("users-list")
