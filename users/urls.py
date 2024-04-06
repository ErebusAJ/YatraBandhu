from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", auth_view.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("",views.landing, name="landing"),
    path("home/", views.home, name='home'),
    path("profile/", views.profile, name="profile"),
    path("update/", views.update_profile, name="profile-update"),
    path('contact/', views.contact, name='contact'),
    path("send-friend-request/<int:to_user_id>/", views.send_friend_request, name="send-friend-request"),
    path("accept-friend-request/<int:friendship_id>/", views.accept_friend_request, name="accept-friend-request"),
    path("reject-friend-request/<int:friendship_id>/", views.reject_friend_request, name="reject-friend-request"),
]