from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView, BiographyView, UserListView, UserUpdateView, ProfileDeleteView, ContactUptadeView, CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetDoneView


urlpatterns = [path("sing-up/", SignUpView.as_view(), name="sign-up"),
               path("login/", CustomLoginView.as_view(), name="login"),
               path("change-password", CustomPasswordChangeView.as_view(), name='change-password'),
               path("logout", LogoutView.as_view(), name="logout"),
               path("users", UserListView.as_view(), name="users-list"),
               path("<int:pk>/contact", ContactUptadeView.as_view(), name="contact"),
               path("<int:pk>/change-profile", UserUpdateView.as_view(), name="change-profile"),
               path("<int:pk>/delete", ProfileDeleteView.as_view(), name="delete-profile"),
               path("<int:pk>", BiographyView.as_view(), name="user-detail"),
               
               path("password-reset", CustomPasswordResetView.as_view(), name="password-reset"),
               path("password-reset/done", CustomPasswordResetDoneView.as_view(), name="password-reset-done")
               # dopisać dwie ścieżki
               # path custompasswordresetconfirmview
               # path custompasswordresetcompleteview
               ]
